from django.contrib import admin
from .models import Accessories, Type


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'accessory_type',
        'name',
        'category',
        'price',
        'image1',
    )

    ordering = ('sku',)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Type, TypeAdmin)
