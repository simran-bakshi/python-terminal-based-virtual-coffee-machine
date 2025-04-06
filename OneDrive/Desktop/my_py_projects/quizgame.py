print("Welcome to Computer Quiz")
playing = input("Do you want to play? ")


if playing.lower()!="yes":
    quit()
print("Okay! Lets play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "Random Acess Memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ")
if answer.lower() == "Read Only Memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the capital of India? ")
if answer.lower() == "Delhi":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")
print("you have got" +  str(score) +  " questions correct!")
print("you have got"  +  str((score/5)*100) + "%.")