from django.db import models
from common.models import Category, Colour, Size


class Kicks(models.Model):

    class Meta:
        verbose_name_plural = 'Kicks'

    category = models.ForeignKey('common.Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    kicks_type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    colour = models.ForeignKey('common.Colour', null=True, blank=True, on_delete=models.SET_NULL)
    sizes_available = models.ForeignKey('common.Size', null=True, blank=True, on_delete=models.SET_NULL)
    default_image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
