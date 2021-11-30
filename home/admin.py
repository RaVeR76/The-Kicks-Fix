""" Administration for Home App """
from django.contrib import admin
from .models import Home, Social, Discount


admin.site.register(Home)
admin.site.register(Social)
admin.site.register(Discount)
