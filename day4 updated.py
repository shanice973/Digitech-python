
print("This program needs the credentials to verify them to grant access to user")  
print() 
users = {
    "shaniz": {"password": "shaniz123@", "role": "admin"},
    "Maxwell": {"password": "max123@", "role": "user"},
    "Malix": {"password": "mal123@", "role": "user"}
}
try:
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")

    if username in users and password == users[username]["password"]:
        print("Welcome!")  
        user_role = users[username]["role"] 

        print(" Main Menu")
        print("1. View Profile")
        print("2. Admin Panel")
        print("3. User Panel")
        print("4. Exit")
        choice = input("Enter your choice: ")  
        if choice == "1":
            print("Showing your profile...")  
            print(f"Name: {username}")  
            print(f"Role: {user_role}")  
        elif choice == "2":
            if user_role == "admin":
                print("Welcome to Admin Panel!")
                print("You have full access.")
            else:
                print("Access Denied! Only admins allowed.")
        elif choice == "3":
            print("Welcome to User Panel!")  
        elif choice == "4":
            print("Goodbye!")  
        else:
            print("Invalid choice!") 
    else:
        print("Wrong username or password!")  
except Exception as e:
    print(f"An error occurred: {e}") 

