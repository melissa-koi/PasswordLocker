#!/usr/bin/python3
from locker import User
from locker import Account

#USER

def create_user(usernameN, passwordN):
    new_user = User(usernameN, passwordN)
    return new_user

def save_user(credentials):
    credentials.save_user()

def delete_user(credentials):
    credentials.delete_user()

def user_exist(user):
    return User.user_exists(user)

def search_username(user):
    return User.find_by_username(user)

def search_password(user):
    return User.find_by_password(user)

#ACCOUNTS

def create_account(username, password):
    new_account = Account(username, password)
    return new_account

def save_account(details):
    details.save_account()

def delete_account(details):
    details.delete_account()

def display_accounts():
    return Account.display_accounts()


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
            print(f"Congratulations {usernamePL}, account creation successful\n")


            print("Would you like to login? Enter y-proceed or n-exit")
            code = input().lower()
            if code == 'y':
                print("Username")
                lgUsername = input()
                print("Password")
                lgPassword = input()

                if search_username(lgUsername) and search_password(lgPassword):
                    print(f"Welcome {usernamePL} to your account!!\n")
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
                print(f"Welcome {usernamePL} to your account!!")
                while True:
                    print(f"Select a short code: sa - store account credentials, ca - create account credentials, dc - display saved credentials, ex - to exit ,d - delete\n")
                    next_code = input().lower()

                    if next_code == 'sa':
                        print("Account Username")
                        a_username = input()
                        print("Account Password")
                        a_password = input()
                        save_account(create_account(a_username,a_password))
                        print(f"Creation of {a_username} account successful\n")

                    elif next_code == 'dc':
                        if display_accounts():
                            print("Here is a list of all your account credentials")
                            print('-'*20)
                            for account in display_accounts():
                                print(f"{account.user_account} ....... password: {account.password}")
                        else:
                            print("You don't seem to have any contacts saved yet\n")

                    elif next_code == 'ex':
                        print("Going to main...")
                        SystemExit

                    elif next_code == 'd':
                        print("Enter account to delete")
                        to_delete = input()
                        if search_account

            else:
                print("Incorrect login credentials\n")


        elif short_code == 'ex':
            print("Bye .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
