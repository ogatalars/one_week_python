class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f'{self.name} says meow!')
        
class Lion(Cat): # Lion inherits from Cat 
    def roar(self):
        print(f'{self.name} says roar!')            