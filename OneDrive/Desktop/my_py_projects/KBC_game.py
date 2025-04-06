#Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.
print("Hello! Would you like to play?")
init = input("(YES/NO:)").strip().upper()
if init == "YES":
    Question = ["Q1: What is the capital of India?"]
    print(Question)
    Answers = {"a": "Lucknow",
           "b": "Banglore",
           "c": "Delhi",
           "d" : "Chennai",
}
    correct_ans = "c".strip()
    print(Answers)
    user_ans =input("Choose your Answer:")
    print(user_ans)
    if user_ans == correct_ans:
        print("Congratulations! You won Rs 100000")
    else:
        print("Incorrect Answer,Better Luck next time")    