from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(jewellery)
admin.site.register(group)
admin.site.register(users)