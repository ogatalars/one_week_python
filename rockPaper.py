import random

computer_choice = random.randint(1, 3)
# rock = 1
# papper = 2
# scissors = 3
your_move = str(input("Rock, Paper, or Scissors? "))

    
if computer_choice == 1:
    print("Computer chose rock")
elif computer_choice == 2:
    print("Computer chose paper")
else:
    print("Computer chose scissors")
    
if your_move == "Rock" and computer_choice == 1:
    print("You tied")
elif your_move == "Rock" and computer_choice == 2:
    print("You lost")
elif your_move == "Rock" and computer_choice == 3:
    print("You won")
elif your_move == "Paper" and computer_choice == 1:
    print("You won")
elif your_move == "Paper" and computer_choice == 2:
    print("You tied")
elif your_move == "Paper" and computer_choice == 3:
    print("You lost")
elif your_move == "Scissors" and computer_choice == 1:
    print("You lost")
elif your_move == "Scissors" and computer_choice == 2:
    print("You won")
else:
    print("You tied")                                       