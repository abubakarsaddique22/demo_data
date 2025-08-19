# from rapidfuzz import process,fuzz
# grocery_products = {
#     "Clothing & Accessories": [
#         "Shirts", "T-Shirts", "Pants", "Jeans", "Jackets", "Sweaters",
#         "Shalwar Kameez", "Saree", "Kurta", "Abaya", "Hijab",
#         "Shoes", "Sandals", "Slippers", "Socks",
#         "Caps", "Hats", "Scarves", "Gloves", "Belts",
#         "Watches", "Sunglasses"
#     ],

#     "Food": [
#         # Grains & Staples
#         "Rice", "Wheat Flour (Atta)", "Maize", "Oats",
#         # Vegetables
#         "Potatoes", "Onions", "Tomatoes", "Spinach", "Carrots",
#         # Fruits
#         "Apples", "Bananas", "Mangoes", "Oranges", "Grapes",
#         # Protein
#         "Chicken", "Mutton", "Beef", "Fish", "Eggs", "Pulses",
#         # Dairy
#         "Milk", "Yogurt", "Cheese", "Butter", "Ghee",
#         # Snacks
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
#         # Furniture
#         "Beds", "Sofas", "Tables", "Chairs", "Cupboards",
#         # Kitchen
#         "Stove", "Fridge", "Microwave", "Blender",
#         "Utensils", "Plates", "Glasses",
#         # Cleaning
#         "Broom", "Mop", "Vacuum Cleaner", "Detergent", "Soap", "Sanitizer",
#         # Bathroom
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




# def correct_spelling(word, choices):
#     best_match, score, _ = process.extractOne(word, choices)
#     return best_match if score > 50 else word

# # Continuous loop
# while True:
#     print("\n===== Grocery Categories =====")
#     categories = list(grocery_products.keys())
    
#     # Show menu with exit option
#     print("0. Exit")
#     for i, cat in enumerate(categories, start=1):
#         print(f"{i}. {cat}")

#     # Take category input
#     choice = input("\nSelect a category (number): ")

#     if not choice.isdigit():
#         print("❌ Please enter a valid number.")
#         continue

#     choice = int(choice)

#     if choice == 0:
#         print("\n✅ Exiting the system. Goodbye!")
#         break

#     if 1 <= choice <= len(categories):
#         selected_category = categories[choice - 1]
#         print(f"\nYou selected: {selected_category}")
#         print("Available products:", grocery_products[selected_category])
        
#         # Take product input
#         user_input = input("\nEnter product names (comma separated): ")
#         user_items = [item.strip() for item in user_input.split(",")]
        
#         # Correct spelling
#         corrected_items = [correct_spelling(item, grocery_products[selected_category]) for item in user_items]
        
#         # Show results
#         print("\nOriginal Input:", user_items)
#         print("Corrected Output:", corrected_items)
#     else:
#         print("❌ Invalid choice. Try again.")



from rapidfuzz import process, fuzz

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

# Flatten all products into one list
all_products = [item for sublist in grocery_products.values() for item in sublist]

def correct_spelling(word, choices):
    best_match, score, _ = process.extractOne(word, choices)
    return best_match if score > 70 else None

# Continuous loop
while True:
    user_input = input("\nEnter product names (comma separated) or type 'exit' to quit: ")
    if user_input.lower() == "exit":
        print("✅ Exiting the system. Goodbye!")
        break

    user_items = [item.strip() for item in user_input.split(",")]
    corrected_items = []

    for item in user_items:
        match = correct_spelling(item, all_products)
        if match:
            corrected_items.append(match)
        else:
            # Not found, suggest related products
            related = process.extract(item, all_products, limit=5, scorer=fuzz.token_sort_ratio)
            related_names = [r[0] for r in related if r[1] > 40]
            print(f"❌ '{item}' is not in stock. Did you mean: {related_names}?")
    
    if corrected_items:
        print("\n✅ Corrected / Available Products:", corrected_items)
