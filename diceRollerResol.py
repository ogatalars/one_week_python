from random import randint
num_dice = int(input('How many dices do you want to roll? '))
num_sides = int(input('How many sides do you want to roll? '))

while True:
   result = '|'
   for die in range(num_dice):
       rand = randint(1, num_sides)
       result += f"{rand}|"    
   print(randint(1, num_sides))
   reply = input('Do you want to roll again? (y/n) ')
   if reply == 'q':
       break
   