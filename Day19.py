
The Programmers Bank - Day 19: Dynamic Dictionary Operations
Author: [Aapka Naam]
Description: A clean bank portal system that demonstrates how to dynamically 
             add new fields and update existing values inside Python Dictionaries.
"""

print("------------------🏦 The Programmers Bank -----------------")

bank_account = {
    "name": "Abdul Basit",
    "balance": 5000,
    "account_type": "Current"
}

print(f"Current Account Holder: {bank_account['name']}")
print(f"Starting Balance: Rs. {bank_account['balance']}\n")


print("--- 📱 Security Update: Register Mobile Number ---")
user_phone = input("Enter your mobile number to link with account: ")


bank_account["phone"] = user_phone
print("✔ Mobile number linked successfully!\n")


print("--- 💰 Transaction: Cash Deposit ---")
try:
    deposit_amount = int(input("Enter the amount you want to deposit: Rs. "))
    
    if deposit_amount > 0:
        # Updating the existing balance value
        bank_account["balance"] += deposit_amount
        print("✔ Deposit successful!")
    else:
        print("❌ Invalid amount. Deposit failed.")
except ValueError:
    print("❌ Error: Please enter a valid number for the amount.")


print("\n------------------ 📄 Updated Bank Profile -----------------")
print(f"Account Holder : {bank_account['name']}")
print(f"Linked Phone   : {bank_account['phone']}")
print(f"Account Type   : {bank_account['account_type']}")
print(f"Updated Balance: Rs. {bank_account['balance']}")
print("------------------------------------------------------------")
