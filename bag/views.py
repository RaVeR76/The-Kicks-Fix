from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from kicks.models import Kicks
from accessories.models import Accessories

# Create your views here.


def view_bag(request):
    """" My Bag view see the user can see their shopping bag so far """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the quantity of selected item to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    size = None

    if 'kids_size' in request.POST:
        size = request.POST['kids_size']
    if 'female_size' in request.POST:
        size = request.POST['female_size']
    if 'male_size' in request.POST:
        size = request.POST['male_size']

    if size:
        kicks = get_object_or_404(Kicks, sku=item_id)
        if item_id in list(bag.keys()):
            if size in bag[item_id]['kicks_by_size'].keys():
                bag[item_id]['kicks_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {kicks.name} quantity to {bag[item_id]["kicks_by_size"][size]}')
            else:
                bag[item_id]['kicks_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {kicks.name} to your bag')
        else:
            bag[item_id] = {'kicks_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {kicks.name} to your bag')
    else:
        accessory = get_object_or_404(Accessories, sku=item_id)
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {accessory.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {accessory.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update the quantity of selected item to the shopping bag by the selected amount """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    size = None
    if 'kicks_size' in request.POST:
        size = request.POST['kicks_size']

    if size:
        kicks = get_object_or_404(Kicks, sku=item_id)
        if quantity > 0:
            bag[item_id]['kicks_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {kicks.name} quantity to {bag[item_id]["kicks_by_size"][size]}')
        else:
            del bag[item_id]['kicks_by_size'][size]
            if not bag[item_id]['kicks_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {kicks.name} from your bag')
    else:
        accessory = get_object_or_404(Accessories, sku=item_id)
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {accessory.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {accessory.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove item from the bag """

    try:
        bag = request.session.get('bag', {})
        size = None
        if 'kicks_size' in request.POST:
            size = request.POST['kicks_size']

        if size:
            kicks = get_object_or_404(Kicks, sku=item_id)
            del bag[item_id]['kicks_by_size'][size]
            if not bag[item_id]['kicks_by_size']:
                bag.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {kicks.name} from your bag')
        else:
            accessory = get_object_or_404(Accessories, sku=item_id)
            bag.pop(item_id)
            messages.success(request, f'Removed {accessory.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
