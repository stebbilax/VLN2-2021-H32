from django.contrib import admin

from .models import Account, PaymentInfo, SearchHistoryEntry

# Register your models here.
admin.site.register(Account)
admin.site.register(PaymentInfo)
admin.site.register(SearchHistoryEntry)