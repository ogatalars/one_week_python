class Dog:
    def __init__(self, name, breed, location ):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        
chorsu = Dog('Chorsu', 'Husky', 46)        
print(chorsu)
print(chorsu.name)
print(chorsu.breed)