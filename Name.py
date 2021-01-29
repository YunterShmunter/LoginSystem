import time
import random

login_or_register = input("Would you like to Login or Register: ")
is_logged_in = False
will_stay = False

if login_or_register == "Login" or login_or_register == "login":
    username = input("\nType your username here: ")
    password = input("\nType your password here: ")
    login = username + password

    with open("Database.txt") as u:
        if login in u.read():
            print("Welcome " + username + ", Get ready to play BlackJack")
            is_logged_in = True
            time.sleep(2)
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

if is_logged_in:
    card_one = random.randint(0, 11)
    card_two = random.randint(0, 10)
    new_card = random.randint(0, 11)
    our_hand = card_one + card_two
    dealers_card_one = random.randint(0, 11)
    dealers_card_two = random.randint(0, 10)
    dealers_new_card = random.randint(0, 11)
    dealers_hand = dealers_card_one + dealers_card_two

    print("Your hand: " + str(card_one), str(card_two) + " = " + str(our_hand))
    print("Dealers hand: " + str(dealers_card_one) + " ?")
    time.sleep(1)

    hit_or_stay = input("Would you like to hit or stay: ")

    if hit_or_stay == "hit" or "Hit":
        print("Hit: " + str(new_card))
        new_hand = our_hand + new_card
        print("New hand: " + str(new_hand))
        hit_or_stay = input("Would you like to hit or stay: ")
    elif hit_or_stay == "stay" or "Stay":
        will_stay = True

    if will_stay and dealers_hand <= 16:
        new_dealers_hand = dealers_hand + dealers_new_card
        print(dealers_card_one, dealers_card_two, dealers_new_card)
    elif will_stay and dealers_hand >= 17:
        print(dealers_card_one, dealers_card_two)
