import random
user_choice = int(input("Enter Your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissor"))
if user_choice >= 3 or user_choice < 0:
    print("You Entered a Invalid Number, You Lose")
else:
    computer_choice = random.randint(0,2)
    print("Computer Choice:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a Draw")
    elif user_choice == 0 and computer_choice == 2 :
        print("You Won")
    elif user_choice == 2 and computer_choice == 0:
        print("You Won")
    elif user_choice < computer_choice:
        print("You Lose")
    elif user_choice > computer_choice :
        print("You Won")