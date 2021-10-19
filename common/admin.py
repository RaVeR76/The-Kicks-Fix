from django.contrib import admin
from .models import Category, Colour, Size


# Register your models here.
admin.site.register(Category)
admin.site.register(Colour)
admin.site.register(Size)
