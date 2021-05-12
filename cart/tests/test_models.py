from django.test import TestCase
from django.contrib.auth.models import User

from cart.models import CartItem
from user.models import Product, Category


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.category = Category.objects.create(name='Cereal')
        self.product = Product.objects.create(name='Cocoa Puffs',
                                              supplier='General Mills',
                                              description='Its great',
                                              price=30,
                                              category=self.category
                                              )
        self.cartItem = CartItem.objects.create(cart=self.user.account.cart,
                                                product=self.product)

    def tearDown(self):
        self.user.delete()

    def test_cart_exists(self):
        self.assertIsNotNone(self.user.account.cart)

    def test_item_is_in_users_cart(self):
        items = CartItem.objects.filter(cart=self.user.account.cart)
        self.assertIsNotNone(items)
        item = items[0].product
        self.assertEqual(item.name, 'Cocoa Puffs')
        self.assertEqual(item.supplier, 'General Mills')
        self.assertEqual(item.description, 'Its great')
        self.assertEqual(item.price, 30)
        self.assertEqual(item.category.name, 'Cereal')
