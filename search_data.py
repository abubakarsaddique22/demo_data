from fuzzywuzzy import process
import re
import pandas as pd
import pandas as pd
import os

def load_product_data():
    """Load product data from CSV or use sample data"""
    try:
        if os.path.exists('all_products.csv'):
            df = pd.read_csv('all_products.csv')
            print("Dataset loaded successfully from all_products.csv!")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Using sample dataset as fallback.")
        # Sample dataset as fallback
        data = [
            ["HELLO HAIR HERBAL SHAMPOO 75ML", "Rs. 160", "In Stock"],
            ["Intense Repair Shampoo for Damaged Hair – 175ML", "Rs. 600", "In Stock"],
            ["Head & Shoulders Silky Black Shampoo 360ML", "Rs. 999", "Out of Stock"],
            ["new Hair Shampoo 360ML", "Rs. 2300", "In Stock"],
            ["Biogain Shampoo for Hairfall", "Rs. 1,650", "Low Stock"],
            ["Set & Touch LONG & STRONG SHAMPOO 180ML", "Rs. 400", "In Stock"],
            ["Dettol Soap Cool", "Rs. 85", "In Stock"]
        ]
        df = pd.DataFrame(data, columns=["title", "price", "stock_status"])
    
    return df
# Global variables for context
last_matched_product = None
last_product_name = None

# Keywords
price_keywords = [
    "how much", "price kya hai", "kitni price", "tell me price", "what is the price",
    "cost kya hai", "price", "kitne ka hai", "kia price hai", "cost", "pricing"
]

availability_keywords = [
    "is available", "in stock", "is this", "do you have", "available", "stock",
    "have", "availability", "stock status"
]

def extract_product_name(query, choices):
    """Extract product name from query using fuzzy matching"""
    # Remove common question words and special characters
    query = re.sub(r'\b(what|is|the|price|cost|available|stock|of|do|you|have|tell|me|about)\b', '', query, flags=re.IGNORECASE)
    query = re.sub(r'[^\w\s]', '', query).strip()
    
    if not query:
        return None, 0
    
    # Try to find the best match
    best_match, score = process.extractOne(query, choices)
    return best_match, score

def search_product(user_input, df):
    global last_matched_product, last_product_name
    
    query = user_input.lower()
    choices = df["title"].tolist()
    
    # Check if user is asking about price
    asking_price = any(word in query for word in price_keywords)
    
    # Check if user is asking about availability
    asking_availability = any(word in query for word in availability_keywords)
    
    # Extract product name from query
    product_name, score = extract_product_name(user_input, choices)
    
    # If we found a product with good confidence, update context
    if score > 50:
        last_product_name = product_name
        matched_row = df[df["title"] == product_name].iloc[0]
        last_matched_product = {
            "title": matched_row["title"], 
            "price": matched_row["price"],
            "stock_status": matched_row.get("stock_status", "In Stock")
        }
    
    # If no product mentioned but we have context from previous query
    elif last_product_name and (asking_price or asking_availability):
        product_name = last_product_name
        matched_row = df[df["title"] == product_name].iloc[0]
        last_matched_product = {
            "title": matched_row["title"], 
            "price": matched_row["price"],
            "stock_status": matched_row.get("stock_status", "In Stock")
        }
    else:
        last_matched_product = None
    
    # Generate response
    if last_matched_product:
        product_name = last_matched_product['title']
        price = last_matched_product['price']
        stock_status = last_matched_product['stock_status']
        
        # Determine if product is in stock
        is_in_stock = stock_status.lower() in ["in stock", "low stock"]
        
        # Build response based on what was asked
        if asking_availability and asking_price:
            message = f"Yes, {product_name} is available. Price: {price}"
            return {
                "product_name": product_name,
                "price": price,
                "stock_status": stock_status,
                "message": message,
                "success": True
            }
        elif asking_availability:
            message = f"Yes, {product_name} is available" if is_in_stock else f"No, {product_name} is not available"
            return {
                "product_name": product_name,
                "stock_status": stock_status,
                "message": message,
                "success": True
            }
        elif asking_price:
            return {
                "product_name": product_name,
                "price": price,
                "message": f"{product_name} - Price: {price}",
                "success": True
            }
        else:
            # If only product name is mentioned
            return {
                "product_name": product_name,
                "message": f"Product: {product_name}",
                "success": True
            }
    
    # If no product could be identified
    if asking_price or asking_availability:
        return {
            "message": "Please specify which product you are asking about.",
            "success": False
        }
    
    return {
        "message": "I couldn't find that product. Please try again with a different name.",
        "success": False
    }