import datetime

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from account.models import Account, PaymentInfo


class AccountTestCase(TestCase):
    """ Testing basic account creation """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )

    def tearDown(self):
        self.user.delete()

    def test_access_through_user(self):
        """ Test that user has access to account correct properties"""
        self.assertEqual(self.user.account.first_name, '')
        self.assertEqual(self.user.account.last_name, '')

    def test_access_through_account(self):
        """ Test that account has access to user correct properties"""
        account = Account.objects.get(user=self.user)
        self.assertEqual(account.user.username, 'TestingBob')
        self.assertEqual(account.user.email, 'bob@bob.com')


class PaymentInfoTestCase(TestCase):
    """ Testing payment info creation"""

    def setUp(self):
        self.user = User.objects.create(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.payment_info = PaymentInfo.objects.create(
            account=self.user.account,
            cvc=223,
            expiration_date=datetime.datetime(2022, 5, 17),
            street_name='bobstreet',
            house_number=12,
            city='Reykjavik',
            postal_code=101,
            name_of_cardholder='Bob Builder',
            card_number='5535-1234-9876-0001'
        )

    def test_access_through_account(self):
        """ Testing accounts access of payment info """
        self.assertEqual(self.user.account.paymentinfo.cvc, 223)
        self.assertEqual(self.user.account.paymentinfo.street_name, 'bobstreet')
        self.assertEqual(self.user.account.paymentinfo.house_number, 12)
        self.assertEqual(self.user.account.paymentinfo.city, 'Reykjavik')
        self.assertEqual(self.user.account.paymentinfo.card_number, '5535-1234-9876-0001')



