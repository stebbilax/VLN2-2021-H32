from django.test import TestCase
from django.contrib.auth.models import User

from order.models import Order


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.order = Order.objects.create(user=self.user,
                                          total_price=9,
                                          street_name='Laugavegur',
                                          house_number=10,
                                          city='Reykjavík',
                                          postal_code=101)

    def tearDown(self):
        self.user.delete()

    def test_order_exists(self):
        self.assertIsNotNone(self.order)

    def test_order_information(self):
        self.assertEqual(self.order.total_price, 9)
        self.assertEqual(self.order.street_name, 'Laugavegur')
        self.assertEqual(self.order.house_number, 10)
        self.assertEqual(self.order.city, 'Reykjavík')
        self.assertEqual(self.order.postal_code, 101)

