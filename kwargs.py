#We can use the ** notation to write functions that accept any number of keyword arguments.
def demo(**kwargs):
    print(kwargs)
demo(name='John', age=30, city='New York')

def print_ages(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value} years old.')

# Gera um dictionary        