from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User


class AccountCreationTestCase(TestCase):
    """ Asserting that a Account is registered for every User Created """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='bob', email='bob@bob.com', password='qwerty'
        )

    def test_account_exists(self):
        """ Test that an account has been created """
        self.assertIsNotNone(self.user.account)

    def test_account_properties(self):
        """ Test that the account has a first and last name"""
        self.assertEqual(self.user.account.first_name, 'John')
        self.assertEqual(self.user.account.last_name, 'Doe')
