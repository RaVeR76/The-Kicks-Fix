""" Models for Accessories App """
from django.db import models
from common.models import Category, Colour


class Accessories(models.Model):
    """ This model is used to create an Accessory """
    class Meta:
        verbose_name_plural = 'Accessories'

    category = models.ForeignKey('common.Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    type = models.ForeignKey('Type', null=True, blank=True,
                             on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    colour = models.ForeignKey('common.Colour', null=True, blank=True,
                               on_delete=models.SET_NULL)
    image1_url = models.URLField(max_length=1024, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2_url = models.URLField(max_length=1024, null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3_url = models.URLField(max_length=1024, null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    """ Type Model for Accessories """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
