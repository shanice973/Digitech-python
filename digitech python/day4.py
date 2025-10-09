# This program checks the user info and validates it
print("This program needs the credentials to verify them to grant access to user")  # Show program purpose
print()  #  a blank line

# List of users with their passwords and roles
users = {
    "shaniz": {"password": "shaniz123@", "role": "admin"},
    "Maxwell": {"password": "max123@", "role": "user"},
    "Malix": {"password": "mal123@", "role": "user"}
}

try:
    # Ask for username and password
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")

    # Check if username and password are correct
    if username in users and password == users[username]["password"]:
        print("Welcome!")  # Successful login
        user_role = users[username]["role"]  # Get user's role

        # Show menu options
        print(" Main Menu")
        print("1. View Profile")
        print("2. Admin Panel")
        print("3. User Panel")
        print("4. Exit")

        choice = input("Enter your choice: ")  # Get menu choice

        if choice == "1":
            print("Showing your profile...")  # Profile option
            print(f"Name: {username}")  # Show username
            print(f"Role: {user_role}")  # Show role
        elif choice == "2":
            # Only admin can access admin panel
            if user_role == "admin":
                print("Welcome to Admin Panel!")
                print("You have full access.")
            else:
                print("Access Denied! Only admins allowed.")
        elif choice == "3":
            print("Welcome to User Panel!")  # User panel option
        elif choice == "4":
            print("Goodbye!")  # Exit option
        else:
            print("Invalid choice!")  # Wrong menu choice
    else:
        print("Wrong username or password!")  # Login failed
except Exception as e:
    print(f"An error occurred: {e}")  # Catch any unexpected errors

