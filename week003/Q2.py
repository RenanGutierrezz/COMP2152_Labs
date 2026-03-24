#Question: Shopping Cart (List - Searching and Removal)
cart = ["apple","banana","milk","apple","eggs" ]
apple_count = cart.count("apple")
print(f"We have {apple_count} apples")
print(f"Position of milk: {cart.index("milk")}")
cart.remove("apple")
print(f"Removing item using pop: {cart.pop()}")
print(f"Is banana in the cart? {"banana" in cart}")
print(f"Final Cart: {cart}")
