print("------------------The Programmers Bank-----------------")
#_____________Variables_____________
UserName = "1"
Pin = "0"
Attempts = 3


#______Change into Numbers_____
UserName1 = input("UserName:     ")
Pin1 = input("Type The Password")
#_____________Code_________________
if UserName1 != UserName and Attempts > 0:
         UserName1 = input(f"Type the Correct UserName:     ")
         while UserName1 != UserName:
             Attempts -= 1
             UserName1 = input(f"Wrong UserName You Have {Attempts} Attempts Left :     ")
             if Attempts == 0:
                 print("Your Account Is Blocked.....")
                 break
#----------------------Pin-----------------------------
if UserName1 == UserName and Attempts > 0:
         
         Pin1 = input("Your User Name is Correct But Type The Pin Again:")
         while Pin1 != Pin:
                 Attempts -= 1
                 Pin1 = input(f"Wrong Pin You Have {Attempts} Attempts Left :     ")
                 if Attempts == 0:
                     print("Your Account Is Blocked.....")
                     break
             
             
             
             