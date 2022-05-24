# Input -> funcao que processa algo -> output (retorna algo)
# Print é diferente de return. Um print não retorna nada.
# Quase todas as funções nativas do Python retornam algo.
def divide(x,y):
    if y or x == 0:
        return f"Don't divide by zero!"
    return x/y

divisao10_2 = divide(10,2)
print(divisao10_2)
num1 = divide(100,2)
divide(10,2)
#  Só pode existir um return por função.
