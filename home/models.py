from django.db import models

# Create your models here.


class Home(models.Model):

    class Meta:
        verbose_name_plural = 'Home'

    name = models.CharField(max_length=254, default='home')
    main_slogan = models.CharField(max_length=254)
    promotion_bar = models.CharField(max_length=254)
    social_icon = models.ForeignKey('Social', null=True, blank=True, on_delete=models.SET_NULL)
    discount_code = models.ForeignKey('Discount', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Social(models.Model):

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

    name = models.CharField(max_length=254, default='discount')
    discount_code = models.CharField(max_length=25)
    discount_percentage = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    free_delivery_threshold = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    standard_delivery_percentage = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return self.name
