# usamos global para definir que uma variavel é global 
def outer():
    global animal
    animal = 'Wolf'
outer()
print(animal)    