"""
This module contains Category and
Size Admin's display choices and
Registers Sex and Colour
"""
from django.contrib import admin
from .models import Category, Colour, Size, Sex


class CategoryAdmin(admin.ModelAdmin):
    """ Category list display with order """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class SizeAdmin(admin.ModelAdmin):
    """ Size list display with order """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour)
admin.site.register(Size, SizeAdmin)
admin.site.register(Sex)
