print("All Squares 1 To 1000000___________________________________")

user = input("Do You Want All Squares Between 1 to 1000000.   (Yes/No)")
if user == "Yes" or "yes" or "han":
    for i in range(1, 100001):
        square = i * i
        print(f"Square of {i} is {square}")
else:
    print("Ok Fine By....")