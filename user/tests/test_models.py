from django.test import TestCase, RequestFactory

from user.models import Product, Category, Keyword


class ProductTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Category.objects.create(name='Cereal')
        Category.objects.create(name='Spoons')
        Category.objects.create(name='Bowls')

    def test_product_category_relationship(self):
        product = Product.objects.create(
            name='Corn Flakes',
            supplier='Nestley',
            description='So amazing',
            price=12.39,
            category=Category.objects.get(name='Cereal')
        )
        self.assertEqual(product.price, 12.39)
        self.assertEqual(product.category.name, 'Cereal')

    def test_product_keyword_relationship(self):
        product = Product.objects.create(
            name='Corn Flakes',
            supplier='Nestley',
            description='So amazing',
            price=12.39,
            category=Category.objects.get(name='Cereal')
        )
        Keyword.objects.create(name='sugary', product=product)
        Keyword.objects.create(name='healthy', product=product)

        keywords = product.keyword_set.all()
        self.assertEqual(len(list(keywords)), 2)
        self.assertEqual(keywords[0].name, 'sugary')
        self.assertEqual(keywords[1].name, 'healthy')
