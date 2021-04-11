import pyperclip

class User:

    user_details = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_account(self):
        User.user_details.append(self)

    def delete_account(self):
        User.user_details.remove(self)

class Account:

    account_details = []
