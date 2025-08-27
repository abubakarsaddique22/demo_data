from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from spell_checker import correct_spelling, suggest_alternatives,all_products
import uvicorn
from pydantic import BaseModel
from typing import Optional
from search_data import load_product_data,search_product


# ------------------------------
# FastAPI app initialization
# ------------------------------

app = FastAPI()

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
# Request & Response Models
# ------------------------------

class ProductQuery(BaseModel):
    query: str

class ProductResponse(BaseModel):
    product_name: Optional[str] = None
    price: Optional[str] = None
    stock_status: Optional[str] = None
    message: str
    success: bool

# ------------------------------
# Home route
# ------------------------------

@app.get("/")
def home():
    return {"message": "API is running. Go to /docs to test endpoints."}

# ------------------------------
# Product spelling correction endpoint
# ------------------------------

@app.post("/correct-products")
async def correct_products(file: UploadFile = File(...)):
    content = await file.read()
    products = [product.strip() for product in content.decode("utf-8").split(',')]

    corrected_items = []
    suggestions = {}

    for item in products:
        item = item.strip()
        if not item:
            continue
        
        # Try to correct the spelling
        corrected = correct_spelling(item)
        
        # If we found a good match and it's different from original, use it
        if corrected and corrected.lower() != item.lower():
            corrected_items.append(corrected)
        # If no good match found, check if it's already correct
        elif not corrected:
            # Item might be already correct or completely irrelevant
            # Check if it exists in our product list (case-insensitive)
            if any(item.lower() == product.lower() for product in all_products):
                corrected_items.append(item)
            else:
                # Item is irrelevant, provide suggestions
                corrected_items.append(item)
                suggestions[item] = suggest_alternatives(item)
        else:
            # Item is already correct
            corrected_items.append(item)

    return {
        "corrected_products": corrected_items,
        "suggestions": suggestions
    }



# ------------------------------
# Product query endpoint
# ------------------------------

@app.post("/query", response_model=ProductResponse)
async def query_product(product_query: ProductQuery):
    """
    Query product information based on user input.
    
    Example queries:
    - "Is Dettol Soap Cool available?"
    - "What is the price of Head & Shoulders shampoo?"
    - "Is Biogain Shampoo in stock and what is its price?"
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
    