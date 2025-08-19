from fuzzywuzzy import process
import pandas as pd

# Sample dataset
data = [
    ["HELLO HAIR HERBAL SHAMPOO 75ML", "Rs. 160"],
    ["Intense Repair Shampoo for Damaged Hair – 175ML", "Rs. 600"],
    ["Head & Shoulders Silky Black Shampoo 360ML", "Rs. 999"],
    ["new Hair Shampoo 360ML", "Rs. 2300"],
    ["Biogain Shampoo for Hairfall", "Rs. 1,650"],
    ["Set & Touch LONG & STRONG SHAMPOO 180ML", "Rs. 400"]
]

df = pd.DataFrame(data, columns=["title", "price"])

# Keywords
price_keywords = [
    "how much", "price kya hai", "kitni price", "tell me price", "what is the price",
    "cost kya hai", "price", "kitne ka hai", "kia price hai"
]

availability_keywords = [
    "is available", "in stock", "is this", "do you have", "available", "stock"
]

last_matched_product = None  # Global variable for context

def find_product(user_input, df):
    global last_matched_product
    query = user_input.lower()
    
    asking_price = any(word in query for word in price_keywords)
    asking_availability = any(word in query for word in availability_keywords)
    
    # Remove keywords to isolate product name
    temp_query = query
    for word in price_keywords + availability_keywords:
        temp_query = temp_query.replace(word, "")
    temp_query = temp_query.replace("and", "").replace("?", "").strip()
    
    # Fuzzy match if user mentioned a product
    if temp_query:
        choices = df["title"].tolist()
        best_match, score = process.extractOne(temp_query, choices)
        if score > 50:
            matched_row = df[df["title"] == best_match].iloc[0]
            # Convert to dictionary to avoid Pandas Series truth value issues
            last_matched_product = {"title": matched_row["title"], "price": matched_row["price"]}
        else:
            last_matched_product = None
    
    # Generate response
    if last_matched_product is not None:
        response = ""
        if asking_availability:
            response += f"Yes, {last_matched_product['title']} is available"
        if asking_price:
            if response:
                response += f" — {last_matched_product['price']}"
            else:
                response += f"{last_matched_product['title']} — {last_matched_product['price']}"
        if not response:  # user only mentioned product, no price/availability
            response = f"{last_matched_product['title']}"
        return response
    
    # If no product context exists but user asked for price/availability
    if (asking_price or asking_availability) and last_matched_product is None:
        return "Please specify which shampoo you are asking about."
    
    # If nothing matched
    return "No close match found."

# ----------------------------
# Example usage
print("Welcome! Ask about any shampoo and I will try to help.")
while True:
    user_query = input("\nEnter your product query: ")
    if user_query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    print(find_product(user_query, df))


