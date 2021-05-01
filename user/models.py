from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=300)
    supplier = models.CharField(max_length=300)
    description = models.TextField(max_length=9000)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Keyword(models.Model):
    name = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductPhoto(models.Model):
    url = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)