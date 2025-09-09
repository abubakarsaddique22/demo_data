# # from rapidfuzz import process, fuzz

# # # === Product List ===
# # grocery_products = {
# #     "Clothing & Accessories": [
# #         "Shirts", "T-Shirts", "Pants", "Jeans", "Jackets", "Sweaters",
# #         "Shalwar Kameez", "Saree", "Kurta", "Abaya", "Hijab",
# #         "Shoes", "Sandals", "Slippers", "Socks",
# #         "Caps", "Hats", "Scarves", "Gloves", "Belts",
# #         "Watches", "Sunglasses"
# #     ],
# #     "Food": [
# #         "Rice", "Wheat Flour (Atta)", "Maize", "Oats",
# #         "Potatoes", "Onions", "Tomatoes", "Spinach", "Carrots",
# #         "Apples", "Bananas", "Mangoes", "Oranges", "Grapes",
# #         "Chicken", "Mutton", "Beef", "Fish", "Eggs", "Pulses",
# #         "Milk", "Yogurt", "Cheese", "Butter", "Ghee",
# #         "Chips", "Biscuits", "Chocolates", "Cakes", "Namkeen"
# #     ],
# #     "Drinks": [
# #         "Water", "Tea", "Green Tea", "Coffee",
# #         "Mango Juice", "Orange Juice", "Apple Juice",
# #         "Coke", "Pepsi", "7Up",
# #         "Red Bull", "Sting", "Monster",
# #         "Milkshake", "Smoothie"
# #     ],
# #     "Household Items": [
# #         "Beds", "Sofas", "Tables", "Chairs", "Cupboards",
# #         "Stove", "Fridge", "Microwave", "Blender",
# #         "Utensils", "Plates", "Glasses",
# #         "Broom", "Mop", "Vacuum Cleaner", "Detergent", "Soap", "Sanitizer",
# #         "Shampoo", "Toothpaste", "Towels", "Toilet Paper"
# #     ],
# #     "Electronics & Gadgets": [
# #         "Smartphone", "Laptop", "Tablet", "Television",
# #         "Refrigerator", "Washing Machine", "Camera",
# #         "Headphones", "Speakers", "Smartwatch", "Fitness Band",
# #         "Charger", "Power Bank"
# #     ],
# #     "Transportation": [
# #         "Car", "Motorbike", "Bicycle", "Bus", "Train",
# #         "Airplane", "Rickshaw", "Metro", "Boat",
# #         "Petrol", "Diesel", "CNG", "Electric Charging"
# #     ],
# #     "Personal Care": [
# #         "Perfume", "Deodorant", "Cream", "Lotion",
# #         "Shaving Kit", "Razor", "Hair Oil", "Hair Dryer",
# #         "Lipstick", "Foundation", "Kajal", "Nail Polish"
# #     ],
# #     "Health & Medicine": [
# #         "First Aid Kit", "Bandages", "Antiseptic", "Painkiller",
# #         "Antibiotics", "Diabetes Medicine", "Hypertension Medicine",
# #         "Vitamins", "Supplements", "Mask", "Sanitizer", "Thermometer"
# #     ],
# #     "Education & Office": [
# #         "Books", "Notebooks", "Pens", "Pencils", "Eraser",
# #         "Bag", "Files", "Calculator", "Whiteboard",
# #         "Computer", "Printer", "Photocopier"
# #     ],
# #     "Entertainment": [
# #         "Toys", "Board Games", "Video Games",
# #         "Football", "Cricket Bat", "Tennis Racket", "Gym Equipment",
# #         "Guitar", "Piano", "Drums"
# #     ],
# #     "Miscellaneous": [
# #         "Ring", "Bracelet", "Necklace",
# #         "Watering Can", "Shovel", "Seeds",
# #         "Dog Food", "Cat Food", "Cage", "Fish Tank"
# #     ]
# # }


# # # Flatten all products
# # all_products = [item for sublist in grocery_products.values() for item in sublist]

# # # === Spelling correction (try auto-correct first) ===
# # def correct_spelling(word):
# #     best_match, score, _ = process.extractOne(word, all_products, scorer=fuzz.token_sort_ratio)

# #     # If confidence is good, return directly (auto-correct)
# #     if score >= 75:
# #         return {"corrected": best_match, "alternatives": []}

# #     # If confidence is medium, return best guess + 2 suggestions
# #     elif 55 <= score < 75:
# #         suggestions = process.extract(word, all_products, limit=3, scorer=fuzz.token_sort_ratio)
# #         return {"corrected": best_match, "alternatives": [s[0] for s in suggestions if s[0] != best_match]}

# #     # If confidence is too low, no correction, just suggest
# #     else:
# #         suggestions = process.extract(word, all_products, limit=5, scorer=fuzz.token_sort_ratio)
# #         return {"corrected": None, "alternatives": [s[0] for s in suggestions]}


# from rapidfuzz import process, fuzz

# # === Product List ===
# grocery_products = {
#     "Clothing & Accessories": [
#         "Shirts", "T-Shirts", "Pants", "Jeans", "Jackets", "Sweaters",
#         "Shalwar Kameez", "Saree", "Kurta", "Abaya", "Hijab",
#         "Shoes", "Sandals", "Slippers", "Socks",
#         "Caps", "Hats", "Scarves", "Gloves", "Belts",
#         "Watches", "Sunglasses"
#     ],
#     "Food": [
#         "Rice", "Wheat Flour (Atta)", "Maize", "Oats",
#         "Potatoes", "Onions", "Tomatoes", "Spinach", "Carrots",
#         "Apples", "Bananas", "Mangoes", "Oranges", "Grapes",
#         "Chicken", "Mutton", "Beef", "Fish", "Eggs", "Pulses",
#         "Milk", "Yogurt", "Cheese", "Butter", "Ghee",
#         "Chips", "Biscuits", "Chocolates", "Cakes", "Namkeen"
#     ],
#     "Drinks": [
#         "Water", "Tea", "Green Tea", "Coffee",
#         "Mango Juice", "Orange Juice", "Apple Juice",
#         "Coke", "Pepsi", "7Up",
#         "Red Bull", "Sting", "Monster",
#         "Milkshake", "Smoothie"
#     ],
#     "Household Items": [
#         "Beds", "Sofas", "Tables", "Chairs", "Cupboards",
#         "Stove", "Fridge", "Microwave", "Blender",
#         "Utensils", "Plates", "Glasses",
#         "Broom", "Mop", "Vacuum Cleaner", "Detergent", "Soap", "Sanitizer",
#         "Shampoo", "Toothpaste", "Towels", "Toilet Paper"
#     ],
#     "Electronics & Gadgets": [
#         "Smartphone", "Laptop", "Tablet", "Television",
#         "Refrigerator", "Washing Machine", "Camera",
#         "Headphones", "Speakers", "Smartwatch", "Fitness Band",
#         "Charger", "Power Bank"
#     ],
#     "Transportation": [
#         "Car", "Motorbike", "Bicycle", "Bus", "Train",
#         "Airplane", "Rickshaw", "Metro", "Boat",
#         "Petrol", "Diesel", "CNG", "Electric Charging"
#     ],
#     "Personal Care": [
#         "Perfume", "Deodorant", "Cream", "Lotion",
#         "Shaving Kit", "Razor", "Hair Oil", "Hair Dryer",
#         "Lipstick", "Foundation", "Kajal", "Nail Polish"
#     ],
#     "Health & Medicine": [
#         "First Aid Kit", "Bandages", "Antiseptic", "Painkiller",
#         "Antibiotics", "Diabetes Medicine", "Hypertension Medicine",
#         "Vitamins", "Supplements", "Mask", "Sanitizer", "Thermometer"
#     ],
#     "Education & Office": [
#         "Books", "Notebooks", "Pens", "Pencils", "Eraser",
#         "Bag", "Files", "Calculator", "Whiteboard",
#         "Computer", "Printer", "Photocopier"
#     ],
#     "Entertainment": [
#         "Toys", "Board Games", "Video Games",
#         "Football", "Cricket Bat", "Tennis Racket", "Gym Equipment",
#         "Guitar", "Piano", "Drums"
#     ],
#     "Miscellaneous": [
#         "Ring", "Bracelet", "Necklace",
#         "Watering Can", "Shovel", "Seeds",
#         "Dog Food", "Cat Food", "Cage", "Fish Tank"
#     ]
# }

# # Flatten all products
# all_products = [item for sublist in grocery_products.values() for item in sublist]


# # === Spelling correction (try auto-correct first) ===
# def correct_spelling(word: str):
#     best_match, score, _ = process.extractOne(word, all_products, scorer=fuzz.token_sort_ratio)

#     # If confidence is good, return directly (auto-correct)
#     if score >= 75:
#         return {"corrected": best_match, "alternatives": []}

#     # If confidence is medium, return best guess + 2 suggestions
#     elif 55 <= score < 75:
#         suggestions = process.extract(word, all_products, limit=3, scorer=fuzz.token_sort_ratio)
#         return {"corrected": best_match, "alternatives": [s[0] for s in suggestions if s[0] != best_match]}

#     # If confidence is too low, no correction, just suggest
#     else:
#         return {"corrected": None, "alternatives": suggest_alternatives(word)}


# # === Suggestion function (independent) ===
# def suggest_alternatives(word: str, limit: int = 5):
#     related = process.extract(word, all_products, limit=limit, scorer=fuzz.token_sort_ratio)
#     return [r[0] for r in related if r[1] > 40]




from rapidfuzz import process, fuzz

# === Product List ===
grocery_products = {
    "Clothing & Accessories": [
        "Shirts", "T-Shirts", "Pants", "Jeans", "Jackets", "Sweaters",
        "Shalwar Kameez", "Saree", "Kurta", "Abaya", "Hijab",
        "Shoes", "Sandals", "Slippers", "Socks",
        "Caps", "Hats", "Scarves", "Gloves", "Belts",
        "Watches", "Sunglasses"
    ],
    "Food": [
        "Rice", "Wheat Flour (Atta)", "Maize", "Oats",
        "Potatoes", "Onions", "Tomatoes", "Spinach", "Carrots",
        "Apples", "Bananas", "Mangoes", "Oranges", "Grapes",
        "Chicken", "Mutton", "Beef", "Fish", "Eggs", "Pulses",
        "Milk", "Yogurt", "Cheese", "Butter", "Ghee",
        "Chips", "Biscuits", "Chocolates", "Cakes", "Namkeen"
    ],
    "Drinks": [
        "Water", "Tea", "Green Tea", "Coffee",
        "Mango Juice", "Orange Juice", "Apple Juice",
        "Coke", "Pepsi", "7Up",
        "Red Bull", "Sting", "Monster",
        "Milkshake", "Smoothie"
    ],
    "Household Items": [
        "Beds", "Sofas", "Tables", "Chairs", "Cupboards",
        "Stove", "Fridge", "Microwave", "Blender",
        "Utensils", "Plates", "Glasses",
        "Broom", "Mop", "Vacuum Cleaner", "Detergent", "Soap", "Sanitizer",
        "Shampoo", "Toothpaste", "Towels", "Toilet Paper"
    ],
    "Electronics & Gadgets": [
        "Smartphone", "Laptop", "Tablet", "Television",
        "Refrigerator", "Washing Machine", "Camera",
        "Headphones", "Speakers", "Smartwatch", "Fitness Band",
        "Charger", "Power Bank"
    ],
    "Transportation": [
        "Car", "Motorbike", "Bicycle", "Bus", "Train",
        "Airplane", "Rickshaw", "Metro", "Boat",
        "Petrol", "Diesel", "CNG", "Electric Charging"
    ],
    "Personal Care": [
        "Perfume", "Deodorant", "Cream", "Lotion",
        "Shaving Kit", "Razor", "Hair Oil", "Hair Dryer",
        "Lipstick", "Foundation", "Kajal", "Nail Polish"
    ],
    "Health & Medicine": [
        "First Aid Kit", "Bandages", "Antiseptic", "Painkiller",
        "Antibiotics", "Diabetes Medicine", "Hypertension Medicine",
        "Vitamins", "Supplements", "Mask", "Sanitizer", "Thermometer"
    ],
    "Education & Office": [
        "Books", "Notebooks", "Pens", "Pencils", "Eraser",
        "Bag", "Files", "Calculator", "Whiteboard",
        "Computer", "Printer", "Photocopier"
    ],
    "Entertainment": [
        "Toys", "Board Games", "Video Games",
        "Football", "Cricket Bat", "Tennis Racket", "Gym Equipment",
        "Guitar", "Piano", "Drums"
    ],
    "Miscellaneous": [
        "Ring", "Bracelet", "Necklace",
        "Watering Can", "Shovel", "Seeds",
        "Dog Food", "Cat Food", "Cage", "Fish Tank"
    ]
}

# Flatten all products
all_products = [item for sublist in grocery_products.values() for item in sublist]

# Spelling correction function
def correct_spelling(word):
    best_match, score, _ = process.extractOne(word, all_products, scorer=fuzz.token_sort_ratio)
    return best_match if score > 70 else None

# Suggest alternatives
def suggest_alternatives(word):
    related = process.extract(word, all_products, limit=5, scorer=fuzz.token_sort_ratio)
    return [r[0] for r in related if r[1] > 40]
