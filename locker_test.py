import unittest
from locker import User
import pyperclip

class TestAccount(unittest.TestCase):

#UserAccount
    def setUp(self):
        self.new_user = User("test_username", "test_password1")

    def tearDown(self):
        User.user_details = []

    def test_init(self):
        self.assertEqual(self.new_user.username, "test_username")
        self.assertEqual(self.new_user.password, "test_password1")

    def test_save_account(self):
        self.new_user.save_account()
        self.assertEqual(len(User.user_details),1)

    def test_save_multiple_accounts(self):
        self.new_user.save_account()
        test_account = User("username2", "password2")
        test_account.save_account()

        self.assertEqual(len(User.user_details),2)

    def test_delete_account(self):
        self.new_user.save_account()
        test_account = User("username2", "password2")
        test_account.save_account()

        self.new_user.delete_account()
        self.assertEqual(len(User.user_details),1)

#AccountDetails