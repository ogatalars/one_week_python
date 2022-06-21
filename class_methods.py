class Puppy:
    species = 'canine'
    
    @classmethod
    def register_anon(cls):
        return cls('Anonymous')
    def __init__(self, name):
        self.name = name
        self.tricks = []