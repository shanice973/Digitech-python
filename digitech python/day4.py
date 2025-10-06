#this program checks the user info and validates it 
print("This program  needs the credentilas to verify them to grant access to user")
print()

username =input("enter your username:  ")
password =input("enter your password:  ")



if username == "shaniz" and password =="shaniz123@" :
    print("Welcome!")
elif username != "shaniz" and password =="shaniz123@":
    print("Check your credentials and Try Again!")
else:
    print("Try Again!")