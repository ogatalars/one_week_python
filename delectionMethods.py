langs = ['python', 'perl', 'ruby', 'c', 'c++', 'java']
langs.clear()
print(langs)
# Langs normalmente limpa a lista!
langs2 = ['python', 'perl', 'ruby', 'c', 'c++', 'java']
langs2.remove('python')
print(langs2)
nums = [1, 2, 3, 4, 5, 6,7, 5, 4, 3, 4, 2]
nums.remove(4)

nums.pop() # Remove o ultimo elemento da lista
last_num = nums.pop()
langs2.pop(0)   # Remove o primeiro elemento da lista

langs3 = ['python', 'perl', 'ruby', 'c', 'c++', 'java']
del langs3[2]
print(langs3)