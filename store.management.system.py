from time import sleep



products = [
    {"name": "Milk", "price": 3.49, "qty": 20, "category": "Dairy"},
    {"name": "Eggs", "price": 2.99, "qty": 12, "category": "Dairy"},
    {"name": "Cheddar Cheese", "price": 4.50, "qty": 15, "category": "Dairy"},
    {"name": "Greek Yogurt", "price": 5.99, "qty": 10, "category": "Dairy"},
    {"name": "Butter", "price": 4.79, "qty": 8, "category": "Dairy"},
    {"name": "Bananas", "price": 0.89, "qty": 30, "category": "Fruits & Veggies"},
    {"name": "Apples", "price": 1.29, "qty": 25, "category": "Fruits & Veggies"},
    {"name": "Avocados", "price": 1.99, "qty": 12, "category": "Fruits & Veggies"},
    {"name": "Tomatoes", "price": 1.49, "qty": 18, "category": "Fruits & Veggies"},
    {"name": "Onions", "price": 0.99, "qty": 20, "category": "Fruits & Veggies"},
    {"name": "Potatoes", "price": 2.49, "qty": 15, "category": "Fruits & Veggies"},
    {"name": "Spinach", "price": 2.29, "qty": 10, "category": "Fruits & Veggies"},
    {"name": "Bell Peppers", "price": 1.79, "qty": 14, "category": "Fruits & Veggies"},
    {"name": "Chicken Breast", "price": 6.99, "qty": 10, "category": "Meat & Seafood"},
    {"name": "Ground Beef", "price": 5.49, "qty": 12, "category": "Meat & Seafood"},
    {"name": "Salmon Fillet", "price": 9.99, "qty": 8, "category": "Meat & Seafood"},
    {"name": "Bacon", "price": 4.99, "qty": 10, "category": "Meat & Seafood"},
    {"name": "Turkey Slices", "price": 3.99, "qty": 12, "category": "Meat & Seafood"},
    {"name": "White Bread", "price": 2.49, "qty": 15, "category": "Bakery"},
    {"name": "Whole Wheat Bread", "price": 2.99, "qty": 12, "category": "Bakery"},
    {"name": "Croissants", "price": 3.49, "qty": 10, "category": "Bakery"},
    {"name": "Bagels", "price": 4.29, "qty": 8, "category": "Bakery"},
    {"name": "Flour Tortillas", "price": 2.19, "qty": 14, "category": "Bakery"},
    {"name": "Rice", "price": 3.99, "qty": 20, "category": "Pantry Staples"},
    {"name": "Pasta", "price": 1.99, "qty": 25, "category": "Pantry Staples"},
    {"name": "Olive Oil", "price": 7.49, "qty": 10, "category": "Pantry Staples"},
    {"name": "Salt", "price": 1.29, "qty": 30, "category": "Pantry Staples"},
    {"name": "Sugar", "price": 2.19, "qty": 25, "category": "Pantry Staples"},
    {"name": "Black Pepper", "price": 2.49, "qty": 20, "category": "Pantry Staples"},
    {"name": "Garlic Powder", "price": 2.99, "qty": 15, "category": "Pantry Staples"},
    {"name": "Canned Beans", "price": 1.49, "qty": 30, "category": "Canned Goods"},
    {"name": "Canned Corn", "price": 1.29, "qty": 25, "category": "Canned Goods"},
    {"name": "Tomato Sauce", "price": 1.99, "qty": 20, "category": "Canned Goods"},
    {"name": "Tuna", "price": 2.49, "qty": 18, "category": "Canned Goods"},
    {"name": "Chicken Soup", "price": 1.79, "qty": 22, "category": "Canned Goods"},
    {"name": "Orange Juice", "price": 3.49, "qty": 15, "category": "Beverages"},
    {"name": "Apple Juice", "price": 2.99, "qty": 12, "category": "Beverages"},
    {"name": "Coke", "price": 5.99, "qty": 20, "category": "Beverages"},
    {"name": "Sparkling Water", "price": 3.49, "qty": 18, "category": "Beverages"},
    {"name": "Coffee Grounds", "price": 6.49, "qty": 10, "category": "Beverages"},
    {"name": "Chips", "price": 3.99, "qty": 25, "category": "Snacks & Candy"},
    {"name": "Pretzels", "price": 2.49, "qty": 20, "category": "Snacks & Candy"},
    {"name": "Chocolate Bar", "price": 1.89, "qty": 30, "category": "Snacks & Candy"},
    {"name": "Granola Bars", "price": 3.49, "qty": 15, "category": "Snacks & Candy"},
    {"name": "Popcorn", "price": 2.29, "qty": 22, "category": "Snacks & Candy"},
    {"name": "Frozen Pizza", "price": 4.99, "qty": 12, "category": "Frozen"},
    {"name": "Ice Cream", "price": 3.99, "qty": 15, "category": "Frozen"},
    {"name": "Frozen Veggies", "price": 2.49, "qty": 20, "category": "Frozen"},
    {"name": "Chicken Nuggets", "price": 5.49, "qty": 10, "category": "Frozen"},
    {"name": "Paper Towels", "price": 2.99, "qty": 25, "category": "Household"},
    {"name": "Dish Soap", "price": 3.49, "qty": 18, "category": "Household"},
    {"name": "Trash Bags", "price": 4.29, "qty": 15, "category": "Household"},
    {"name": "Aluminum Foil", "price": 2.79, "qty": 20, "category": "Household"}
]

def sell_items(name, quantity_sold):
    found = False
    for i in products:
        if i["name"].lower() == name.lower():
            found = True
            if i["qty"] >= quantity_sold:
                i["qty"] -= quantity_sold
                print("Product sold successfly!")
                print("Remaining stock of", i["name"], ":", i["qty"])
            else:
                print("Not enough stock available.")
    if not found:
        print("Product not found.")


def update_product():
    name = input("Enter the name of the product you want to update: ").lower()
    found = False
    for i in products:
        if i["name"].lower() == name.lower():
            found = True
            new_price = input("Enter new price (leave blank to keep current): ")
            new_quantity = input("Enter new quantity (leave blank to keep current): ")
            if new_price != "":
                i["price"] = float(new_price)
            if new_quantity != "":
                i["qty"] = int(new_quantity)
            print("Product updated successfully!")
            break

    if not found:
        print("Product not found.")



def add_product(name,price,category,quantity):
    product={"name":name,"price":price,"category":category, "qty":quantity}
    products.append(product)





while True:
    print("-------------------------")
    print("Store management system")
    print("1.Add product")
    print("2.view all products")
    print("3.Update price/stock")
    print("4.sell a products")
    print("5.Show low-stock items")
    print("6.Exit")
    choice=int(input("Enter your choice:('1-6')"))
    print("-------------------------")
    if choice== 1 :
        print("Add a new prduct section:")
        print("=====================================")
        print("Please fill the following questions:(type exit to exit this section)")
        print("=====================================")
        name=input("Enter product name:")
        if name =="exit":
            print("Exiting the add-product section...")
            sleep(2)
            continue
        price=input("Enter product price:")
        if price=="exit":
            print("Exsiting the section...")
            sleep(2)
            continue
        price=float(price)
        quantity=input("Enter product quantity:")
        if quantity =="exit":
            print("Exsiting the section...")
            sleep(2)
            continue
        quantity=int(quantity)
        category=input("Enter product category:")
        if category == "exit":
            print("Exsiting the section...")
            sleep(2)
            continue
        add_product(name,price,category,quantity)
        print("-----------------------------")
        print("Product added successfully!")
        print("-----------------------------")
    elif choice == 2:
        print("All products section:")
        print("--------------------------------")
        for i in products:
            print("Name:",i["name"],"|","Price:",i["price"],"|","Quantity:",i["qty"],"|","Category:",i["category"])
            print("--------------------------------")
    elif choice == 3:
        print("update price/stock section:")
        print("--------------------------------")
        update_product()

    elif choice == 4:
        print("-------------------------")
        print("Sell a product section:")
        print("-------------------------")
        name=input("Enter the name of your product")
        quantity_sold=int(input("Enter the quantity you want to sell:"))
        sell_items(name,quantity_sold)

    elif choice == 5:
        print("Low stock items section:")
        found_low= False
        for item in products:
            if item["qty"]< 5:
                print("Name:",item["name"],"|","Price:",item["price"],"|","Quantity:",item["qty"],"|","Category:",item["category"])
                print("--------------------------------")
                found_low=True
        if not found_low:
            print("All products are well stocked.")

    
    elif choice == 6:
        print("Exciting the store managment system...")
        print("Programm shutdown in 4 seconds...")
        sleep(2)
        print("3")
        sleep(2)
        print("2")
        sleep(2)
        print(1)
        sleep(2)
        break