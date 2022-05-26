# Every variable we work with in python has a scope or boundary where it can be used. There are specific rules to how variables are scoped based on where they are initialyy defined.
# Global Scope => variaveis declaradas fora de funcoes são do tipo global. TODAS as funcções tem acesso à elas.
animal = 'Lemur'
print('Outside the function:', animal)
def func():
    print('Inside the function:', animal)
    def inner_func():
        print('Inside innerFunc function:', animal)
    inner_func()
func()    

#  Local Scope => variaveis declaradas dentro de funcoes são do tipo local.
def cube(num):
    answer: int = num ** 3
    print(answer)
print(cube(1))
# print(answer)    nao vai imprimir nada
for char in 'OCTOPUS':
    color= 'magenta'
    print(char)
print('After the loop:', color)
# Variaveis declaradas dentro do for, podem ser acessadas fora do for, o que é diferente de funções.


# Enclosing Scope
# Nested 'inner ' functions have access to variables declared in outer parent functions
def outside():
    a = 10
    def inside():
        print('a is:' , a)
    inside()        
    
#Built-in scope
num  =5
str(num)    # tem um escopo somente dessa posição
print(num)
 
# Order de escopos
animal = 'Wolf'
def outer():
    animal = 'Echdina'
    print(animal)
    
outer()    
# Ele muda o valor de animal
# A ordem é Local => Enclosing => global => Built-in
