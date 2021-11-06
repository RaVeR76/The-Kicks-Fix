from decimal import Decimal
from django.conf import settings
from home.models import Discount


def bag_contents(request):

    site_discounts = Discount.objects.get(name='discount')

    bag_items = []
    total = 0
    kicks_count = 0
    accessories_count = 0

    free_delivery_threshold = site_discounts.free_delivery_threshold
    standard_delivery_percentage = site_discounts.standard_delivery_percentage

    if total < free_delivery_threshold:
        delivery = total * standard_delivery_percentage / 100
        free_delivery_topup = free_delivery_threshold - total
    else:
        delivery = 0
        free_delivery_topup = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'kicks_count': kicks_count,
        'accessories_count': accessories_count,
        'free_delivery_topup': free_delivery_topup,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
