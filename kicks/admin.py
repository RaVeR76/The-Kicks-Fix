"""
This module contains Kicks, Brands and
Styles Admin's display choices
"""
from django.contrib import admin
from .models import Kicks, Brand, Style


class KicksAdmin(admin.ModelAdmin):
    """ Kicks list display with order """
    list_display = (
        'brand',
        'sku',
        'name',
        'sex',
        'category',
        'price',
        'image1',
    )

    ordering = ('brand',)


class BrandAdmin(admin.ModelAdmin):
    """ Kicks Brands list display with order """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class StyleAdmin(admin.ModelAdmin):
    """ Kicks Styles list display with order """
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Kicks, KicksAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Style, StyleAdmin)
