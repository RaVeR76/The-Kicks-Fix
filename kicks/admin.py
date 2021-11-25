from django.contrib import admin
from .models import Kicks, Brand, Style

# Register your models here.


class KicksAdmin(admin.ModelAdmin):
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
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Kicks, KicksAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Style, StyleAdmin)
