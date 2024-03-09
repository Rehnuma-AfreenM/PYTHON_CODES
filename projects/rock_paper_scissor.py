import random

options = ["rock", "paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number =random.randint(0,2)
    computer_input = options[random_number]
    print("computer chooses ", computer_input)

    if user_input=="rock" and computer_input == "scissor":
        print("You win")

        
    elif user_input=="paper" and computer_input == "rock":
        print("You win")    
        
 

    elif user_input=="scissor" and computer_input == "paper":
        print("You win") 

    else:
        print("you lose")             
    