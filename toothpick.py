print('Welcome to the toothpick game!')
print("*********************************")
player1 = str(input('Enter your name: '))
player2 = str(input('Enter your name: '))
num_left = 13

while True:
    print("   " * num_left)
    
    print(f"there are {num_left} left")
    p1_choice = int(input(f"{player1}'s turn. How many do you take? : "))
    num_left -= p1_choice
    print(" " * num_left)
    if num_left <= 0:
        print(f"{player1} wins!")
        break
    
    p2_choice = int(input(f"{player2}'s turn. How many do you take? : "))
    num_left -= p2_choice
    print(" " * num_left)
    if num_left <= 0:
        print(f"{player2} wins!")
        break
    

