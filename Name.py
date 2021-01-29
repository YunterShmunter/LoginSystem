import time
import random

login_or_register = input("Would you like to Login or Register: ")
is_logged_in = False
blackjack_deck = [1, 12]
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
    dealers_hand = card_one + card_two

    print(card_one, card_two + " = " + our_hand)
    hit_or_stay = input("Would you like to hit or stay: ")

    if hit_or_stay == "hit" or "Hit":
        print("Hit: " + str(new_card))
        new_hand = our_hand + new_card
        print(str(our_hand) + str(new_card))