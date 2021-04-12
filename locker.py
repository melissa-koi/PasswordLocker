import pyperclip

class User:
    """
    Class that handles generating accounts for login into PasswordLocker
    """
    user_details = []

    def __init__(self, user_name, password):
        """
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New User username.
            password : New User's password.
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_details
        """
        User.user_details.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from the user_details
        """
        User.user_details.remove(self)

    @classmethod
    def find_by_username(cls, username):
        """
        find a user by username
        """
        for name in cls.user_details:
            if name.user_name == username:
                return name.user_name

    @classmethod
    def find_by_password(cls, password):
        """
        find a user by password
        """
        for passwrd in cls.user_details:
            if passwrd.password == password:
                return passwrd.password


class Account:
    """
    Class that handles accounts
    """
    account_details = []

    def __init__(self, user_account, password):
        self.user_account = user_account
        self.password = password
        """
        __init__ method that helps us define properties for our objects.
    
        Args:
            user_account: New account username.
            password : New account password.
        """
    def save_account(self):
        """
        save_account method saves account objects into account_details
        """
        Account.account_details.append(self)

    def delete_account(self):
        """
        delete_account method deletes a saved account from the account_details
        """
        Account.account_details.remove(self)

    @classmethod
    def display_accounts(cls):
        """
        method that returns a list of all accounts saved
        """
        return cls.account_details

    @classmethod
    def find_account(cls, account_name):
        """
        find an account using account_name
        """
        for name in cls.account_details:
            if name.user_account == account_name:
                return name

    @classmethod
    def copy_account_name(cls, account_name):
        """
        Copying the user_account
        """
        account_found = Account.find_account(account_name)
        pyperclip.copy(account_found.user_account)