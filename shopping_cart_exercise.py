# Write a Python script that does the following:

# - Prints out a “banner” to welcome users to our shop
# - Asks the user for the name of the item they are buying
# - Asks the user for the price of that item
# - Asks the user for the quantity they are purchasing
# - Prints out a message that includes their subtotal (quantity 𝚡 price)

print("*************WELCOME TO OUR USELESS SHOP STORE**************")
name = str(input("What is the name of the item you are buying? "))
price = float(input("What is the price of the item you are buying? "))
quantity =float(input("How many of the item you are buying? "))
print(f"your item is {name} and the subtotal is {quantity * price}, thank you for shopping with us!")


# usando uma função seria assim:
#     def shopping_cart():
#         name = str(input("What is the name of the item you are buying? "))
#         price = float(input("What is the price of the item you are buying? "))
#         quantity =float(input("How many of the item you are buying? "))
#         print(f"your item is {name} and the subtotal is {quantity * price}, thank you for shopping with us!")
# shoopint_cart()