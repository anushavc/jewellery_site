from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(jewellery)
admin.site.register(users)
admin.site.register(order)
admin.site.register(OrderItem)
admin.site.register(shippingaddress)