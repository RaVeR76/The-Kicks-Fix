""" Shopping Bag Contexts """
from django.shortcuts import get_object_or_404
from home.models import Discount
from kicks.models import Kicks
from accessories.models import Accessories


def bag_contents(request):
    """
    This function calculates bag totals,
    minus delivery and shows
    contents 'bag' on whole application
    """
    site_discounts = Discount.objects.get(name='discount')
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    free_delivery_threshold = site_discounts.free_delivery_threshold
    standard_delivery_percentage = site_discounts.standard_delivery_percentage

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Accessories, sku=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Kicks, sku=item_id)
            for size, quantity in item_data['kicks_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
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
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_topup': free_delivery_topup,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }

    return context
