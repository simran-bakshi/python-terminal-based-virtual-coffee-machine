def Add ():
    return a + b
def Sub ():
    return a - b
def Mul ():
    return a * b
def Div ():
    return a / b if b !=0 else print("Error!")
def Floor_Div ():
    return a // b if b !=0 else print("Error!")
def wrong ():
    print("You've entered the wrong choice.") 

Operations = {
        "1": "Add",
        "2": "Sub",
        "3": "Mul",
        "4": "Div",
        "5": "Floor Div",
    }

a = int(input("enter first number:"))
b =int(input("enter second number:"))
select = int(input("select operations:"))
if select == 1 :
    print (Add())
elif select == 2 :
    print (Sub())
elif select == 3 :
    print (Mul())
elif select == 4 :
    print (Div())
elif select == 3 :
    print(Floor_Div())
else:
    print("Error!")

 


   


