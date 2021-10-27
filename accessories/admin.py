from django.contrib import admin
from .models import Accessories, Type


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'accessory_type',
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('accessory_type',)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Type, TypeAdmin)
