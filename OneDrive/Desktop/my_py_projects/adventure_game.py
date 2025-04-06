sname = input("Type your name: ")
print(f"Welcome {name} to this adventure.")

# First choice: left or right
answer = input("You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? ").lower().strip()

if answer == "left":
    answer = input("You come to a river. You can walk around or swim across. Type 'walk' to walk around and 'swim' to swim across: ").lower().strip()
    
    if answer == "swim":
        print("You swim across and were eaten by an alligator :(")
    elif answer == "walk":
        print("You walked for many miles, you ran out of water and you lost the game.")
    else:
        print("Invalid option!")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back): ").lower().strip()
    
    if answer == "back":
        print("You go back and lose :(")
    elif answer == "cross":
        answer = input("You crossed the bridge and meet a stranger. Do you want to talk to him? (yes/no): ").lower().strip()
        
        if answer == "yes":
            print("You talked to the stranger. He gave you gold and you win!")
        elif answer == "no":
            print("You ignored the stranger and you lose.")    
        else:
            print("Invalid option!")
    else:
        print("Invalid option!")

else:
    print("Invalid option!")

