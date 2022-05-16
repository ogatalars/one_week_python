import random 
number_aleatorio = random.randint(1,6)
number_aleatorio2 = random.randint(1,6)
count = 1

while number_aleatorio !=1 or number_aleatorio2 != 1:
    print(number_aleatorio, number_aleatorio2)
    number_aleatorio = random.randint(1,6)
    number_aleatorio2 = random.randint(1,6)
    count += 1

print("Snake eyes")
print(f"Demorou {count} vezes")