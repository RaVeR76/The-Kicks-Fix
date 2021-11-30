"""
This module contains Accessories and
Types Admin's display choices
"""
from django.contrib import admin
from .models import Accessories, Type


class AccessoriesAdmin(admin.ModelAdmin):
    """ Accessories list display with order """
    list_display = (
        'sku',
        'type',
        'name',
        'category',
        'price',
        'image1',
    )

    ordering = ('sku',)


class TypeAdmin(admin.ModelAdmin):
    """ Accessories Types list display with order """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Type, TypeAdmin)
