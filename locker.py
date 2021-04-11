import pyperclip

class User:

    user_details = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        User.user_details.append(self)

    def delete_user(self):
        User.user_details.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for name in cls.user_details:
            if name.user_name == username:
                return name.user_name

    @classmethod
    def find_by_password(cls, password):
        for passwrd in cls.user_details:
            if passwrd.password == password:
                return passwrd.password

    @classmethod
    def user_exists(cls, user):
        for name in cls.user_details:
            if name.user_details == user:
                return True
        return False


class Account:

    account_details = []

    def __init__(self, user_account, password):
        self.user_account = user_account
        self.password = password

    def save_account(self):
        Account.account_details.append(self)

    def delete_account(self):
        Account.account_details.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.account_details



    def __str__(self):
        return f"a contact for {self.user_account} __str__"

    def __repr__(self):
        return f"a contact for {self.user_account} __repr__"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_account}, {self.password!r})"