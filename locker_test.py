import unittest
from locker import User
import pyperclip

class TestAccount(unittest.TestCase):


    def setUp(self):
        self.new_user = User("test_username", "test_password1")

    def tearDown(self):
        User.user_details = []

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "test_username")
        self.assertEqual(self.new_user.password, "test_password1")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)

    def test_save_multiple_accounts(self):
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        self.assertEqual(len(User.user_details),2)

    def test_delete_account(self):
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_details),1)

    def test_username_exists(self):
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        found_username = User.find_by_username("username2")
        self.assertEqual(found_username.user_name, test_account.user_name)

