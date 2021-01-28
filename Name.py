import time

login_or_register = input("Would you like to Login or Register: ")

if login_or_register == "Login" or login_or_register == "login":
    username = input("\nType your username here: ")
    password = input("\nType your password here: ")
    login = username + password

    with open("Database.txt") as u:
        if login in u.read():
            print("Welcome " + username + ", you are now logged in!")
            is_logged_in = True
            time.sleep(1)
            print("Type play to play a game of BlackJack")
        else:
            print("Incorrect Username Or Password")
elif login_or_register == "Register" or login_or_register == "register":
    register_username = input("\nType the username you want to have: ")
    register_password = input("\nType the password you want to have: ")
    register_username = register_username + register_password
    confirm_password = input("\nConfirm your password by typing it again: ")

    Create_Account = open("Database.txt", "a")
    Check_Account = open("Database.txt", "r")

    if register_username in Check_Account:
        print("That username already exists")
        Create_Account.close()
    elif register_password == confirm_password:
        Create_Account.write("\n" + register_username)
        print("You are now registered")
    else:
        print("Password Does not match")

    Create_Account.close()
else:
    print("Invalid Input")

if is_logged_in == True and input("") == "Play" or "play":
    print("Playing an epic game of BlackJack")