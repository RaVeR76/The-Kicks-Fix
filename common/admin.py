from django.contrib import admin
from .models import Category, Colour, Size, Sex


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


class SizeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour)
admin.site.register(Size, SizeAdmin)
admin.site.register(Sex)
