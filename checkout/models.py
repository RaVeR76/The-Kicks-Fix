""" Models for Checkout App """
import uuid

from django.db import models
from django.db.models import Sum

from django_countries.fields import CountryField

from kicks.models import Kicks
from accessories.models import Accessories
from home.models import Discount
from profiles.models import UserProfile


class Order(models.Model):
    """ This is the order model used to create orders """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        # Utilise Django admin for discounts & delivery costs
        site_discounts = Discount.objects.get(name='discount')

        free_delivery_threshold = site_discounts.free_delivery_threshold
        standard_delivery_percentage = (
            site_discounts.standard_delivery_percentage)

        self.order_total = self.lineitems.aggregate(Sum(
            'lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < free_delivery_threshold:
            self.delivery_cost = self.order_total * (
                standard_delivery_percentage / 100)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    This will create a single line item on order
    """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    kicks = models.ForeignKey(Kicks, null=True, blank=True,
                              on_delete=models.CASCADE)
    accessory = models.ForeignKey(Accessories, null=True, blank=True,
                                  on_delete=models.CASCADE)
    product_size = models.CharField(max_length=8, null=True,
                                    blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product_size:
            self.lineitem_total = self.kicks.price * self.quantity
            super().save(*args, **kwargs)
        else:
            self.lineitem_total = self.accessory.price * self.quantity
            super().save(*args, **kwargs)

    def __str__(self):
        if self.product_size:
            return f'SKU {self.kicks.sku}'\
                   f' on order {self.order.order_number}'
        else:
            return f'SKU {self.accessory.sku}'\
                   f' on order {self.order.order_number}'
