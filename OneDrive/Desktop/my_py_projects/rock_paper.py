import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input== "q":
      break

    if user_input not in options:
        continue   
    random_number = random.randint(0,2)
# rock:0, paper:1, scissor:1

    computer_pick = options[random_number]
# Selects a computer's choice from the options list using random_number as the index
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won! :)")
        user_wins +=  1 

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins +=  1 

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins +=  1 
    
    elif user_input == computer_pick:
        print("It is a tie!")

    else:
        print("You lost! :( ")
        computer_wins +=1
       

print(f"You won {user_wins} times.")
#another method
print("Computer won",computer_wins,"times.")
# Commas separate items in print() and add spaces automatically
print("Goodbye! :)")