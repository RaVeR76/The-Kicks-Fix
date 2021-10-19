from django.contrib import admin
from .models import Kicks, Brand, Type

# Register your models here.

class KicksAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Kicks, KicksAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Type, TypeAdmin)
