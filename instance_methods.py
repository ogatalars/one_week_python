# Add a method! -> this add_trick() method appends a new trick to a puppy instance's tricks list 

class Puppy:
    def __init__(self, name):
        self.name = name 
        self.tricks = []
        
    def add_trick(self, new_trick):
        self.tricks.append(new_trick)
        
sabrina = Puppy('Sabrina')
sabrina.tricks
sabrina.add_trick('sit')
print(sabrina.tricks)        