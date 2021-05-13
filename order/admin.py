from django.contrib import admin
from order.models import Order, OrderContains


# Register your models here.
admin.site.register(Order)
admin.site.register(OrderContains)