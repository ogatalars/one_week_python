# Ideia de usar ID para checar a referência na memoria
print(id(34))
print(id(42))
print(id(34))
print(id(42))
# print(id(34))
# print(id(42))
# print(id(34))
# print(id(42))
# print(id(34))
# print(id(42))
# print(id(34))
# print(id(42))

# This is different from lists. When you create a list, it creates a new object.
# print(id([]))
# print(id([]))
# Quando nós usamos uma lista com um valor e depois apontamos outra lista como atribuida a ela, ocorre que elas apontam para o mesmo objeto/referencia.

lista = [1, 2, 3]
lista2 = lista
print(id(lista))
print(id(lista2))