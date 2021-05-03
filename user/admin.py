from django.contrib import admin
from user.models import Product, ProductPhoto, Category, Keyword


# Register your models here.
admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(Category)
admin.site.register(Keyword)