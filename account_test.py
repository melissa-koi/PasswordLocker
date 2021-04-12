import unittest
from locker import Account
import pyperclip

class TestAccount(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_account = Account("test_user_account", "test_password1")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Account.account_details = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_account.user_account, "test_user_account")
        self.assertEqual(self.new_account.password, "test_password1")

    def test_save_account(self):
        """
        test_save_account test case to test if the account object is saved into
         the account_details
        """
        self.new_account.save_account()
        self.assertEqual(len(Account.account_details),1)

    def test_save_multiple_accounts(self):
        """
        test_save_multiple_accounts to check if we can save multiple account
        objects to our account_details
        """
        self.new_account.save_account()
        test_account = Account("user_account2", "password2")
        test_account.save_account()

        self.assertEqual(len(Account.account_details),2)

    def test_delete_account(self):
        """
        test_delete_account to test if we can remove an account from our account list
        """
        self.new_account.save_account()
        test_account = Account("user_account2", "password2")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_details),1)

    def test_display_all_accounts(self):
        """
        test to check if we can return a list of all accounts saved
        """
        self.assertEqual(Account.display_accounts(), Account.account_details)

    def test_find_account(self):
        """
        test to check if we can find an account using account_name
        """
        self.new_account.save_account()
        test_account = Account("user_account2", "password2")
        test_account.save_account()

        found_account = Account.find_account("user_account2")
        self.assertEqual(found_account.user_account,test_account.user_account)

    def test_copy_account_name(self):
        """
        Test to confirm that we are copying the user_account
        """
        self.new_account.save_account()
        Account.copy_account_name("test_user_account")
        self.assertEqual(self.new_account.user_account, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()