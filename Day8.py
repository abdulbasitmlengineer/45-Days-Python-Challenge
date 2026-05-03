Name = input("What Is Your Name?........       ")
print("____________________________________")
CurrentYear = input("Write Current Year?......        ")
print("____________________________________")
BirthYear = input("In Which Year do you Born?........      ")
print("____________________________________")


BirthYear = int(BirthYear)
CurrentYear = int(CurrentYear)
CalculatedAge = CurrentYear - BirthYear

print(f"You Are {CalculatedAge} years old.")
print("____________________________________")


if CalculatedAge < 18:
    print("Abhi Mehnat Kro Adult Hony main Time Hai....")
else:
    print("Apply Kro Kisi Industry Main.....")

print("__________________________________________")
print("..........Calculator........")
print("______________________________")

user = input("Kia Tum Calculator Use krna Chahoge?.......(Yes/No) ")

if user == "Yes":
    Pehla = int(input("Pehla Number Likho..       "))
    Dosra = int(input("Dosra Number Likho....     "))
    operation = input("Kia Krna Chahte Ho???  (+,-,*,÷) ")

    print("_____________________________")
    print("Here Are the Results.......")
    
    if operation == "+":
        print(f"Addition: {Pehla + Dosra}")
    elif operation == "-":
        print(f"Subtraction: {Pehla - Dosra}")
    elif operation == "*":
        print(f"Multiply: {Pehla * Dosra}")
    elif operation == "÷":
        if Dosra != 0:
            print(f"Division: {Pehla / Dosra}")
        else:
            print("0 se divide Nahi Hota...")
else:
    print("Ok Bye.....")

print(f"Thanks For Using {Name}, Allah Hafiz")
