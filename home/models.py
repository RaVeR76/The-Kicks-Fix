""" Models for Home App """
from django.db import models


class Home(models.Model):
    """ This model will create site requirements """
    class Meta:
        verbose_name_plural = 'Home'

    name = models.CharField(max_length=254, default='home')
    main_slogan = models.CharField(max_length=254)
    promotion_bar = models.CharField(max_length=254)
    social_icon = models.ForeignKey('Social', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    discount_code = models.ForeignKey('Discount', null=True, blank=True,
                                      on_delete=models.SET_NULL)
    main_logo_url = models.URLField(max_length=1024, null=True, blank=True)
    main_logo = models.ImageField(null=True, blank=True)
    toast_logo_url = models.URLField(max_length=1024, null=True, blank=True)
    toast_logo = models.ImageField(null=True, blank=True)
    loader_logo_url = models.URLField(max_length=1024, null=True, blank=True)
    loader_logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    """ This model will create Social Items """
    class Meta:
        verbose_name_plural = 'Social'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Discount(models.Model):
    """ This model will create Discount / Delivery options """

    name = models.CharField(max_length=254, default='discount')
    discount_code = models.CharField(max_length=25)
    discount_percentage = models.DecimalField(max_digits=2,
                                              decimal_places=0, default=0)
    free_delivery_threshold = models.DecimalField(max_digits=2,
                                                  decimal_places=0, default=0)
    standard_delivery_percentage = models.DecimalField(max_digits=2,
                                                       decimal_places=0,
                                                       default=0)

    def __str__(self):
        return self.name
