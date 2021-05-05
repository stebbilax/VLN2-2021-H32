from django.test import TestCase, Client
from django.contrib.auth.models import User

from cart.models import Cart, CartItem
from user.models import Product


class ChangeQuantityTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.product = Product.objects.get(id=1)
        self.cartItem = CartItem.objects.create(self.user.cart, self.product)
        self.client = Client()

    def tearDown(self):
        self.user.delete()
        self.car

    def test_item_is_in_users_cart(self):
        item = CartItem.objects.filter(cart=self.user.cart)
        print(item)
        self.assertTrue(True)
