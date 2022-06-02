# padrões que envolvem listas
lando_2022_results = [4, 3, 5, 8, 3, 5, 5, 5, 5, 4, 14, 10, 2, 7, 7, 9, 10, 10, 9, 10, 8]

# total = 0
# for num in lando_2022_results:
#     total += num

# avg = total/len(lando_2022_results)
# print(total,avg )    -> PADRAO DE RESPOSTA 
def average (nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)    

# Outro padrão de loop para verificar o menor numero 
min = lando_2022_results
for num in lando_2022_results:
    if num < min:
        min = num
print(min)        