from django.test import TestCase, Client
from cart.models import Cart, CartItem
from django.contrib.auth.models import User


class ChangeQuantityTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.client = Client()

    def tearDown(self):
        pass


