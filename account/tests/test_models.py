from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User

from account.models import Account, PaymentInfo, SearchHistoryEntry


# Create your tests here.
class AccountTestCase(TestCase):
    """ Testing basic account creation """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='bob', email='bob@bob.com', password='qwerty'
        )
        self.account = Account.objects.create(user=self.user, first_name='Bob', last_name='Builder')

    def test_access_through_user(self):
        """ Test that user has access to account correct properties"""
        self.assertEqual(self.user.account.first_name, 'Bob')
        self.assertEqual(self.user.account.last_name, 'Builder')

    def test_access_through_account(self):
        """ Test that account has access to user correct properties"""
        account = Account.objects.get(id=self.account.id)
        self.assertEqual(account.user.username, 'bob')
        self.assertEqual(account.user.email, 'bob@bob.com')
