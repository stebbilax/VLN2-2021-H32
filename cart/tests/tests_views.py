from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from cart.models import Cart, CartItem
from user.models import Product, Category
from cart.views import increase_quantity, decrease_quantity


class ChangeQuantityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.wrong_user = User.objects.create(
            username='TestingBill', email='bill@bill.com', password='qwerty'
        )
        self.category = Category.objects.create(name='Cereal')
        self.product = Product.objects.create(name='Cocoa Puffs',
                                              supplier='General Mills',
                                              description='Its great',
                                              price=30,
                                              category=self.category
                                              )
        self.cartItem = CartItem.objects.create(cart=self.user.cart,
                                                product=self.product)
        self.factory = RequestFactory()

    def tearDown(self):
        self.user.delete()

    def test_cart_exists(self):
        self.assertIsNotNone(self.user.cart)

    def test_default_quantity(self):
        """ Default quantity should be one """
        self.assertEqual(self.cartItem.quantity, 1)

    def test_increase_quantity(self):
        """ Quantity should increase by one """
        url = reverse('increase_quantity', args=str(self.cartItem.id))
        request = self.factory.post(url)
        request.user = self.user

        increase_quantity(request, self.cartItem.id)
        item = CartItem.objects.get(id=self.cartItem.id)
        self.assertTrue(item.quantity == 2)

    def test_decrease_quantity(self):
        """ Quantity should decrease by one """
        increase_url = reverse('increase_quantity', args=str(self.cartItem.id))
        decrease_url = reverse('decrease_quantity', args=str(self.cartItem.id))
        increase_request = self.factory.post(increase_url)
        decrease_request = self.factory.post(decrease_url)
        increase_request.user = self.user
        decrease_request.user = self.user

        # First increase quantity twice
        increase_quantity(increase_request, self.cartItem.id)
        increase_quantity(increase_request, self.cartItem.id)
        # Then decrease by one
        decrease_quantity(decrease_request, self.cartItem.id)

        item = CartItem.objects.get(id=self.cartItem.id)
        self.assertTrue(item.quantity == 2)

    def test_increase_wrong_user(self):
        """ Quantity should stay the same """
        url = reverse('increase_quantity', args=str(self.cartItem.id))
        request = self.factory.post(url)
        request.user = self.wrong_user

        increase_quantity(request, self.cartItem.id)
        item = CartItem.objects.get(id=self.cartItem.id)
        self.assertTrue(item.quantity == 1)

    def test_decrease_wrong_user(self):
        """ Quantity should stay the same """
        url = reverse('decrease_quantity', args=str(self.cartItem.id))
        request = self.factory.post(url)
        request.user = self.wrong_user

        decrease_quantity(request, self.cartItem.id)
        item = CartItem.objects.get(id=self.cartItem.id)
        self.assertTrue(item.quantity == 1)
