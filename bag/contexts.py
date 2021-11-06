from decimal import Decimal
from django.shortcuts import get_object_or_404
from home.models import Discount
from kicks.models import Kicks
from accessories.models import Accessories


def bag_contents(request):

    site_discounts = Discount.objects.get(name='discount') # Utilise Django admin for discounts & delivery costs
    bag_items = []
    total = 0
    kicks_count = 0
    accessories_count = 0
    bag = request.session.get('bag', {})

    free_delivery_threshold = site_discounts.free_delivery_threshold
    standard_delivery_percentage = site_discounts.standard_delivery_percentage

    for item_id, quantity in bag.items():
        if "RAVE" not in item_id: # If No RAVE then it's a Kicks Item
            kicks = get_object_or_404(Kicks, sku=item_id)
            total += quantity * kicks.price
            kicks_count += quantity
            bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'kicks': kicks,
            })
        elif "RAVE" in item_id: # If RAVE then it's an Accessories Item
            accessories = get_object_or_404(Accessories, sku=item_id)
            total += quantity * accessories.price
            accessories_count += quantity
            bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'accessories': accessories,
            })

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
