import os.path

#define the name of the user file
user_file = "Username.txt"

def register():
    #get the username and password from the user
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    #check if the user is already exists
    if os.path.exists(user_file):
        with open("username.txt","a")as file:
            for line in file:
                existing_username = line.strip().split(",")
                if existing_username == username:
                    print("username already exists. please choose a different username.")
                    return

    #add the new user to the file
    with open("username.txt","a")as file:
        file.write(f"{username},{password}\n")

        print("Registration Successfully")

def login():
    #get the username and password from the user
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    #check if the user is exists and the password is correct
    if os.path.exists(user_file):
        with open("username.txt","a")as file:
            for line in file:
                existing_username, existing_password = line.strip().split(",")
                if existing_username == username and existing_password == password:
                    print("Login Successfully.")
                    return

    print("Incorrect username or password")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")