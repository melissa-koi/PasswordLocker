import unittest
from locker import Account
import pyperclip

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.new_account = Account("test_username", "test_password1")

    def tearDown(self):
        Account.account_details = []

    def test_init(self):
        self.assertEqual(self.new_account.username, "test_username")
        self.assertEqual(self.new_account.password, "test_password1")

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(Account.account_details),1)

    def test_save_multiple_accounts(self):
        self.new_account.save_account()
        test_account = Account("username2", "password2")
        test_account.save_account()

        self.assertEqual(len(Account.account_details),2)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("username2", "password2")
        test_account.save_account()

        self.new_account.delete_account()
        self.assertEqual(len(Account.account_details),1)