# multiple loops running on the same time

for outer in range(1, 6):
    print(outer)
    for inner in range(1,5):
        print('\t', inner)
        
for char in "CAT":
    for x in range(3):
        print(char)        