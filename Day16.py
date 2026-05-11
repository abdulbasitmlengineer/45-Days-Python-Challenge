users = ["Abdul Basit", "Sara", "Irfa", "Sami"]
print("Initial Users:", users)

new_user = input("Enter new  name to register: ")
users.append(new_user)
print("After Registration:", users)

user_to_del = input("Enter user name to delete: ")
if user_to_del in users:
    users.remove(user_to_del)
    print("User Deleted.")
else:
    print("User not found.")

users.sort()
print("Final Alphabetical List:", users)
