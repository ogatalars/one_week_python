# args
# We can use the wildcard or * notation to write function that accept any number of arguments.
def avarage(*args):
    return sum(args) / len(args)
# esse * na verdade se traduz em colete todos os argumentos recebidos dentro de uma tupla.

def count_stuff(*args):
    print(args)
count_stuff(1,23,6,7,8,9,0,100)    