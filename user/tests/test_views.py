from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse

from ..views import product_page

from user.models import Product, Category


class ProductPageTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(
            username='TestingBob', email='bob@bob.com', password='qwerty'
        )
        self.category = Category.objects.create(name='TestCategory')
        self.product = Product.objects.create(name='TestProduct',
                                              supplier='TestSupplier',
                                              description='TestDescription',
                                              price=1,
                                              category=self.category)
        self.good_url = reverse('product', args=[self.product.id])

    def tearDown(self):
        self.user.delete()

    def test_add_to_cart_new_item(self):
        request = self.factory.post(self.good_url)
        request.user = self.user
        product_page(request, self.product.id)
        cart_items = self.user.account.cart.cartitem_set.all()

        self.assertEqual(len(cart_items), 1)
        cart_item = cart_items[0]
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 1)

    def test_add_to_cart_already_present_item(self):
        request = self.factory.post(self.good_url)
        request.user = self.user
        product_page(request, self.product.id)
        product_page(request, self.product.id)
        cart_items = self.user.account.cart.cartitem_set.all()

        self.assertEqual(len(cart_items), 1)
        cart_item = cart_items[0]
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)
