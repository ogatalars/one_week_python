# Class Atributes -> species is defined on the class itself -> all isntances of puppy will have the same value for species 

class Puppy: 
    species = 'canine'
    def __init__(self, name):
        self.name = name 
        self.tricks = []