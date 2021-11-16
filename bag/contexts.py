from decimal import Decimal
from django.shortcuts import get_object_or_404
from home.models import Discount
from kicks.models import Kicks
from accessories.models import Accessories


def bag_contents(request):

    site_discounts = Discount.objects.get(name='discount') # Utilise Django admin for discounts & delivery costs
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    free_delivery_threshold = site_discounts.free_delivery_threshold
    standard_delivery_percentage = site_discounts.standard_delivery_percentage

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Accessories, sku=item_id) # I know Accessories has no sizes
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Kicks, sku=item_id) # I know Kicks has sizes
            for size, quantity in item_data['kicks_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

  #  for item_id, quantity in bag.items():
   #     if "RAVE" not in item_id: # If No RAVE then it's a Kicks Item
   #         product = get_object_or_404(Kicks, sku=item_id)
   #         total += quantity * product.price
   #         product_count += quantity
   #         bag_items.append({
   #             'item_id': item_id,
   #             'quantity': quantity,
   #             'product': product,
   #         })
    #    elif "RAVE" in item_id: # If RAVE then it's an Accessories Item
    #        product = get_object_or_404(Accessories, sku=item_id)
    #        total += quantity * product.price
    #        product_count += quantity
    #        bag_items.append({
    #            'item_id': item_id,
    #            'quantity': quantity,
    #            'product': product,
    #        })

     #   elif "RAVE" in item_id: # If RAVE then it's an Accessories Item
      #      product = get_object_or_404(Accessories, sku=item_id)
         #   total += quantity * product.price
         #   accessories_count += quantity
         #   bag_items.append({
         #   'item_id': item_id,
         #   'quantity': quantity,
         #   'product': product,
         #   })

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
