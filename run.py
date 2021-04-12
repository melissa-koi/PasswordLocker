#!/usr/bin/python3
from locker import User
from locker import Account
import string
import secrets

#USER

def create_user(usernameN, passwordN):
    """
    Function to create a new user
    """
    new_user = User(usernameN, passwordN)
    return new_user


def save_user(credentials):
    """
    Function to save user
    """
    credentials.save_user()


def delete_user(credentials):
    """
    Function to delete a user
    """
    credentials.delete_user()


def search_username(user):
    """
    Function to find user using username
    """
    return User.find_by_username(user)


def search_password(user):
    """
    Function to find user using password
    """
    return User.find_by_password(user)


#ACCOUNTS

def create_account(username, password):
    """
    Function to create a new account
    """
    new_account = Account(username, password)
    return new_account


def save_account(details):
    """
    Function to save account
    """
    details.save_account()


def delete_account(details):
    """
    Function to delete an account
    """
    details.delete_account()


def display_accounts():
    """
    Function that returns all the saved accounts
    """
    return Account.display_accounts()


def search_account_name(account_name):
    """
    Function to find an account using account_name
    """
    return Account.find_account(account_name)


def main():

    print("Welcome to Password Locker!!")
    while True:
        print("Select a short code to navigate: ca - create a password locker account, lg - to login, ex - exit")

        short_code = input().lower()

        if short_code == 'ca':
            print("Create username")
            usernamePL = input()

            print("Create password")
            passwordPL = input()

            save_user(create_user(usernamePL, passwordPL))
            print(f"Congratulations {usernamePL}, Password Locker account creation successful!\n")

            print("Would you like to login? Enter y-proceed or n-exit")
            code = input().lower()
            if code == 'y':
                print("Username")
                lgUsername = input()
                print("Password")
                lgPassword = input()

                if search_username(lgUsername) and search_password(lgPassword):
                    print(f"Welcome {usernamePL} to your account!!\n")
                    while True:
                        print(f"Select a short code: sa - store account credentials, ca - create account credentials, dc - display saved credentials, ex - to exit ,d - delete")
                        next_code = input().lower()

                        if next_code == 'sa':
                            print("Account Username")
                            a_username = input()
                            print("Account Password")
                            a_password = input()
                            save_account(create_account(a_username,a_password))
                            print(f"{a_username} account saved\n")

                        elif next_code == 'dc':
                            if display_accounts():
                                print("Here is a list of all your account credentials:")
                                print('-'*20)
                                for account in display_accounts():
                                    print(f"{account.user_account} ....... password: {account.password}")
                                print('-'*20)
                            else:
                                print("You don't seem to have any contacts saved yet\n")

                        elif next_code == 'ex':
                            print("Going to main...\n")
                            break

                        elif next_code == 'd':
                            print("Enter account to delete")
                            to_delete = input()
                            search_account = search_account_name(to_delete)
                            if search_account:
                                delete_account(search_account)
                                print(f"{to_delete} account deleted")
                            else:
                                print(f"You don't seem to have {to_delete} account saved\n")

                        elif next_code == 'ca':
                            print("Create username")
                            ca_name = input()
                            print("Enter gp - to generate a random password or cp - to put in your own password")
                            ca_code = input()

                            if ca_code == 'cp':
                                print("Create Password")
                                ca_password = input()
                                save_account(create_account(ca_name, ca_password))
                                print(f"Creation of {ca_name} account successful\n")

                            elif ca_code == 'gp':
                                print("What is your preferred length for the password?")
                                glength = int(input())
                                alphabet = string.ascii_letters + string.digits
                                gPassword = ''.join(secrets.choice(alphabet) for i in range(glength))
                                print(f"Generated password: {gPassword}")
                                save_account(create_account(ca_name, gPassword))
                                print(f"Creation of {ca_name} account credentials successful\n")

                            else:
                                print("I didn't quite get that. Please use the short codes")

                        else:
                            print("I didn't quite get that. Please use the short codes")
                else:
                    print("Incorrect login credentials\n")

            elif code == 'n':
                print("Bye .......\n")
                SystemExit

            else:
                print("I really didn't get that. Please use enter y or n!\n")

        elif short_code == 'lg':
            print("Username")
            lgUsername = input()
            print("Password")
            lgPassword = input()

            if search_username(lgUsername) and search_password(lgPassword):
                print(f"Welcome {lgUsername} to your account!!\n")
                while True:
                    print(f"Select a short code: sa - store account credentials, ca - create account credentials, dc - display saved credentials, ex - to exit ,d - delete")
                    next_code = input().lower()

                    if next_code == 'sa':
                        print("Account Username")
                        a_username = input()
                        print("Account Password")
                        a_password = input()
                        save_account(create_account(a_username,a_password))
                        print(f"{a_username} account saved\n")

                    elif next_code == 'dc':
                        if display_accounts():
                            print("Here is a list of all your account credentials")
                            print('-'*20)
                            for account in display_accounts():
                                print(f"{account.user_account} ....... password: {account.password}")
                            print('-'*20)
                        else:
                            print("You don't seem to have any contacts saved yet\n")

                    elif next_code == 'ex':
                        print("Going to main...\n")
                        break

                    elif next_code == 'd':
                        print("Enter account to delete")
                        to_delete = input()
                        search_account = search_account_name(to_delete)
                        if search_account:
                            delete_account(search_account)
                            print(f"{to_delete} account deleted\n")
                        else:
                            print(f"You don't seem to have {to_delete} account saved\n")

                    elif next_code == 'ca':
                        print("Create username")
                        ca_name = input()
                        print("Enter gp - to generate a random password or cp - to put in your own password")
                        ca_code = input()

                        if ca_code == 'cp':
                            print("Create Password")
                            ca_password = input()
                            save_account(create_account(ca_name, ca_password))
                            print(f"Creation of {ca_name} account successful\n")

                        elif ca_code == 'gp':
                            print("What is your preferred length for the password?")
                            glength = int(input())
                            alphabet = string.ascii_letters + string.digits
                            gPassword = ''.join(secrets.choice(alphabet) for i in range(glength))
                            print(f"Generated password: {gPassword}")
                            save_account(create_account(ca_name, gPassword))
                            print(f"Creation of {ca_name} account successful\n")

                        else:
                            print("I didn't quite get that. Please use the short codes")

                    else:
                        print("I didn't quite get that. Please use the short codes")
            else:
                print("Incorrect login credentials\n")

        elif short_code == 'ex':
            print("Bye .......")
            break

        else:
            print("I didn't quite get that. Please use the short codes\n")


if __name__ == '__main__':
    main()

