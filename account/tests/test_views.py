from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout


class AccountCreationTestCase(TestCase):
    """ Asserting that a Account is registered for every User Created """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )

    def test_account_exists(self):
        """ Test that an account has been created """
        self.assertIsNotNone(self.user.account)

    def test_account_properties(self):
        """ Test that the account has a first and last name"""
        self.assertEqual(self.user.account.first_name, 'John')
        self.assertEqual(self.user.account.last_name, 'Doe')


class LoginTestCase(TestCase):
    """ Asserting that a registered user can log in and that a non registered user cannot"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )

    def test_login_with_correct_credentials(self):
        user = authenticate(username='TestingBob', password='qwerty')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_login_with_wrong_password(self):
        user = authenticate(username='TestingBob', password='amazingPassword')
        self.assertTrue(user is None)

    def test_login_with_wrong_username(self):
        user = authenticate(username='TestingBill', password='qwerty')
        self.assertTrue(user is None)



