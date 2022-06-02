lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
listaTotal = lista1 + lista2
print(listaTotal)
# This not change lista1 or lista2
print(lista1 * 2) # [1, 2, 3, 1, 2, 3]
colors = ["red", "green", "blue", 'black']
response = input('What color do you want to add to the list? ')
while response.lower() not in colors:
    response = input ('Please enter a valid color: ')

print(f"ok, {response} will be added to the list")

# in is used to see existance of an element in a list
 