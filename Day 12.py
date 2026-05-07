Balance = 5000
Correct_pin = 1234
Attempts = 0

print("-------------Welcome to the Digital Bank---------------")

while Attempts < 3:
    user = int(input("Write the Correct Pin:    "))
    Attempts = Attempts + 1
    if user == Correct_pin: 
        print("Access Guaranteed...")
        withdraw = int(input("How Much Money Do You Want To Withdraw:   "))
        if withdraw <= Balance:
         Balance = Balance - withdraw
         print(f"Transaction Successfull...Balance :         {Balance}...")                 
        else:
                withdraw = int(input("Type A Value According To Your Balance....")) 
        break
     
    else:
            remaining = 3 - Attempts 
            print(f"You Have {remaining} Attempts left...")
if Attempts == 3 and user != Correct_pin:                        
            print("Your Account Is Blocked ....")
            
            
  