from django.db import models
from common.models import Category, Colour, Size, Sex


class Kicks(models.Model):

    class Meta:
        verbose_name_plural = 'Kicks'

    category = models.ForeignKey('common.Category', null=True, blank=True, on_delete=models.SET_NULL)
    sex = models.ForeignKey('common.Sex', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    style = models.ForeignKey('Style', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    colour = models.ForeignKey('common.Colour', null=True, blank=True, on_delete=models.SET_NULL)
    image1_url = models.URLField(max_length=1024, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2_url = models.URLField(max_length=1024, null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3_url = models.URLField(max_length=1024, null=True, blank=True)
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


class Style(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
