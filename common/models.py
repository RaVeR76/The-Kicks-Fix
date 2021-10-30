from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Colour(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=254)

    def __str__(self):
        return self.size


class Sex(models.Model):
    sex = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'sex'

    def __str__(self):
        return self.sex
