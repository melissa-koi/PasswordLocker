import unittest
from locker import User


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
        self.new_user = User("test_username", "test_password1")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_details = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name, "test_username")
        self.assertEqual(self.new_user.password, "test_password1")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the user_details
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple user
        objects to our user_details
        """
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        self.assertEqual(len(User.user_details),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_details),1)

    def test_find_by_username(self):
        """
        test to check if we can find a user by username
        """
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        found_username = User.find_by_username("username2")
        self.assertEqual(found_username, test_account.user_name)

    def test_find_by_password(self):
        """
        test to check if we can find a user by password
        """
        self.new_user.save_user()
        test_account = User("username2", "password2")
        test_account.save_user()

        found_password = User.find_by_password("password2")
        self.assertEqual(found_password, test_account.password)


if __name__ == '__main__':
    unittest.main()