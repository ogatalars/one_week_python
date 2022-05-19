import random 
manyDices = int(input('How many dices do you want to roll? '))
# diceRolls = random.randint(1,6)

for times in range(manyDices):
    diceRolls = random.randint(1,6)
    print(diceRolls)
    
wantAgain = str(input('Do you want to roll again? (y/n) '))
    
if wantAgain == 'y':
    print('Rolling again...')
    for times in range(manyDices):
        diceRolls = random.randint(1,6)
        print(diceRolls)
else:
            print('fim de jogo')    