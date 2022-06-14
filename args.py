# args
# We can use the wildcard or * notation to write function that accept any number of arguments.
def avarage(*args):
    return sum(args) / len(args)
# esse * na verdade se traduz em colete todos os argumentos recebidos dentro de uma tupla.

def count_stuff(*args):
    print(args)
count_stuff(1,23,6,7,8,9,0,100)    

def count_stuff2(*args):
    print(f'You passed me {len(args)} arguments.')

count_stuff2(1,2,3,4,5,6,6)

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
sum(1,2,3,4,5,6,7,8,9,10)

def silly(first, second, *others):
    print(f'First is : {first}')
    print(f'Second is : {second}')
    print(f'Others are : {others}')