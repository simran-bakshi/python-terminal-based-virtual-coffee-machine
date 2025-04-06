import random

print("Welcome to my Number Guesser.")
playing = input("Would you like to play? Yes/No: ")
if playing.lower()!="yes":
    quit()
print("Okay! Lets play :)")

top_of_range = input("Type a number (negative numbers will be accepted): ")

try:
    top_of_range = int(top_of_range)  
except ValueError:
    print("Please type a valid number next time.")
    quit()  
if top_of_range <= 0:
    print("You entered a number less than or equal to zero. Let's proceed anyway!")

# abs() returns the absolute value of a number. For example, abs(-5) returns 5.
random_number = random.randint(1, abs(top_of_range))
while True:
    user_guess = input("Make a guess: ")
    if user_guess.lstrip('-').isdigit(): 
        user_guess = int(user_guess)  
    else:
        print("Please type a valid number next time.")
        continue  
    if user_guess == random_number:
        print("Yay! You got it!")
        break  
    else:
        print("You got it wrong! Try again.")
 