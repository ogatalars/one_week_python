class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        print(f'{self.name} says meow!')
class Lion(Cat):
    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name
    def roar(self):
        print(f'{self.name} says {self.pride_name}!')



# Use super() to refer to the base or parent class. In this case, we use super() to access the __init__ method on from the Cat Class.
 