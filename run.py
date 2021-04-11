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

#ACCOUNTS

def create_account(username, password):
    new_account = Account(username, password)

def main():






if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
