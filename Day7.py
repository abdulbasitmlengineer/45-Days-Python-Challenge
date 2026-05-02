print("Basic Calculator 2026")
print("________________________________________________")
name = input("What is Your Name: ")
number1 = input("Type a number:   ")
number2 = input("Type a number:   ")
print("____________________________________")
number1 = int(number1)
number2 = int(number2)
print("_____________________________")
user = input("Select a operation (+,-,*,÷)")
print("_____________________________")

print(f"Hello {name} Here Are Your Results Allahhafiz.....")

if user == "+":
  print(f"Addition:   {number1 + number2}")

elif user == "-":
  print(f"Subtraction:   {number1 - number2}")
  
elif user == "*":
    print(f"Multiplication:   {number1 * number2}")
        
elif user == "÷":
       if number2 != 0:
            print(f"Division:   {number1 /number2}")
       else:
           print("Bhai 0 se devide Nahi Hota...")
else:
    print("Chose Only Operations....(+,-,*,÷")
    
    