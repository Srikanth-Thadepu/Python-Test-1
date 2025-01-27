def add_item(cart):
    item_name = input("Enter the item name: ")
    try:
        item_price = float(input("Enter the item price: "))
        if item_price < 0:
            print("Price cannot be negative. Try again.")
        else:
            cart.append({"name": item_name, "price": item_price})
            print(f"Added {item_name} to the cart for Rs.{item_price:.2f}.")
    except ValueError:
        print("Invalid price. Please enter a valid number.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item['name']} - Rs.{item['price']:.2f}")

def calculate_total(cart):
    total = sum(item['price'] for item in cart)
    print(f"\nThe total price of items in your cart is Rs.{total:.2f}.")

def shopping_cart():
    cart = []
    while True:
        print("\nShopping Cart Menu")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_item(cart)
            elif choice == 2:
                view_cart(cart)
            elif choice == 3:
                calculate_total(cart)
            elif choice == 4:
                print("Thank you for using the shopping cart. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

shopping_cart()
