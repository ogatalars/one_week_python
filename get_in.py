order = {'cost': 3.5, 'quantity': 12}
print(12 in order) # False
print('cost' in order) # True

prices = {
    'arugala': 1.19, 
    'basil': 2.45, 
    'blackBerries': 3.99,
    'coconut': 4.99,
    'fennel': 5.99,
    'Canela': 6.99,
    'garlic': 0.99,
}
print(prices.get('garlic'))
product = input('What product would you like to buy? ')
price = prices[product]
print(f"That will be ${price}")

# o In só olha as keys

# dict.get() => The get() method will look for a given key in a dictionary. If the key exists, it will return the 
# corresponding value. If the key does not exist, it will return None.
