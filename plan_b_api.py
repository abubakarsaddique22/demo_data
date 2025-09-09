from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from spell_checker import correct_spelling, suggest_alternatives, all_products
import uvicorn
from pydantic import BaseModel, constr
from typing import List, Optional, Dict
from search_data import load_product_data, search_product

# ------------------------------
# FastAPI app initialization
# ------------------------------
app = FastAPI(title="Product Correction & Query API")

# ------------------------------
# Load product data
# ------------------------------
df = load_product_data()

# ------------------------------
# Add CORS middleware
# ------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# ------------------------------
# Pydantic Models
# ------------------------------

class ProductQuery(BaseModel):
    query: constr(strip_whitespace=True, min_length=1)

class ProductResponse(BaseModel):
    product_name: Optional[str] = None
    price: Optional[str] = None
    stock_status: Optional[str] = None
    message: str
    success: bool

# ✅ For spelling correction
class CorrectionResult(BaseModel):
    original: str
    corrected: str
    confidence: float
    suggestions: List[str] = []

class CorrectionResponse(BaseModel):
    corrected_products: List[CorrectionResult]

# ------------------------------
# Home route
# ------------------------------
@app.get("/")
def home():
    return {"message": "API is running. Go to /docs to test endpoints."}

# ------------------------------
# Product spelling correction endpoint
# ------------------------------
@app.post("/correct-products", response_model=CorrectionResponse)
async def correct_products(file: UploadFile = File(...)):
    if not file.filename.endswith((".txt", ".csv")):
        raise HTTPException(status_code=400, detail="Only .txt or .csv files allowed")

    content = await file.read()
    products = [product.strip() for product in content.decode("utf-8").split(',')]

    corrected_items: List[CorrectionResult] = []

    for item in products:
        item = item.strip()
        if not item:
            continue

        corrected = correct_spelling(item)
        score = 0.0
        suggestions = []

        if corrected and corrected.lower() != item.lower():
            score = 0.9  # high confidence if corrected
            corrected_items.append(
                CorrectionResult(
                    original=item,
                    corrected=corrected,
                    confidence=score,
                    suggestions=[]
                )
            )
        elif not corrected:
            # Check if already valid product
            if any(item.lower() == product.lower() for product in all_products):
                score = 1.0
                corrected_items.append(
                    CorrectionResult(
                        original=item,
                        corrected=item,
                        confidence=score,
                        suggestions=[]
                    )
                )
            else:
                # No match found, suggest alternatives
                suggestions = suggest_alternatives(item)
                score = 0.2 if suggestions else 0.0
                corrected_items.append(
                    CorrectionResult(
                        original=item,
                        corrected=item,
                        confidence=score,
                        suggestions=suggestions
                    )
                )
        else:
            # Item already correct
            score = 1.0
            corrected_items.append(
                CorrectionResult(
                    original=item,
                    corrected=item,
                    confidence=score,
                    suggestions=[]
                )
            )

    return CorrectionResponse(corrected_products=corrected_items)

# ------------------------------
# Product query endpoint
# ------------------------------
@app.post("/query", response_model=ProductResponse)
async def query_product(product_query: ProductQuery):
    """
    Query product information based on user input.
    """
    try:
        result = search_product(product_query.query, df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

# ------------------------------
# Run app
# ------------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
