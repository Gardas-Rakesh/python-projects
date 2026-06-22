cart = {}
products = {
    1: {"name": "Pizza", "price": 200},
    2: {"name": "Burger", "price": 100},
    3: {"name": "Pasta", "price": 150},
    4: {"name": "Sandwich", "price": 120},
    5: {"name": "Fries", "price": 80},
    6: {"name": "Coke", "price": 50}
}

def view_products():
    print("\n----Available Products----")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")

def add_to_cart():
    view_products()
    try:
        pid = int(input("Enter the product ID to add to cart: "))
        if pid in products:
            qty = int(input("Enter the quantity: "))
            if pid in cart:
                cart[pid]['quantity'] += qty
            else:
                cart[pid] = {
                    "name": products[pid]['name'],
                    "price": products[pid]['price'],
                    "quantity": qty
                }
            print(f"Added {qty} {products[pid]['name']} to cart.")
        else:
            print("Invalid product ID.")

    except ValueError:
        print("Please enter a valid number.")

def remove_from_cart():
    if not cart:
        print("Your cart is empty.")
        return
    view_cart()

    try:
        pid = int(input("Enter the product ID to remove quantity: "))

        if pid in cart:
            qty = int(input("Enter quantity to remove: "))
            if qty==cart[pid]['quantity']:
                del cart[pid]
                print(f"Removed all {products[pid]['name']} from cart.")
            elif qty <= cart[pid]['quantity']:
                cart[pid]['quantity'] -= qty
                name = cart[pid]['name']
                print(f"Removed {qty} {name} item's from cart.")
            else:
                print("You don't have that much quantity in cart.")
        else:
            print("Product not found in cart.")

    except ValueError:
        print("Enter a valid number.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\n----Your Cart----")
        total = 0

        for pid, item in cart.items():

            name = item['name']
            price = item['price']
            qty = item['quantity']

            subtotal = price * qty
            total += subtotal
            print(f"{pid}.{name} x {qty} = ₹{subtotal}")
        print(f"Total Amount: {total}")

def checkout():
    if not cart:
        print("Your cart is empty.")
        return
    view_cart()

    confirm = input("Do you want to checkout? (yes/no): ")

    if confirm.lower() == "yes":
        print("Order placed successfully! Thank you.")
        cart.clear()
    else:
        print("Checkout cancelled.")
def display_menu():
    while True:
        print("\n---Welcome to Swiggy App---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            view_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            remove_from_cart()
        elif choice == '4':
            view_cart()
        elif choice == '5':
            checkout()

        elif choice == '6':
            print("Thank you for using Swiggy App!")
            break

        else:
            print("Invalid choice.")
            
display_menu()