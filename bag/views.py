from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

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
        if item_id in list(bag.keys()):
            if size in bag[item_id]['kicks_by_size'].keys():
                bag[item_id]['kicks_by_size'][size] += quantity
            else:
                bag[item_id]['kicks_by_size'][size] = quantity
        else:
            bag[item_id] = {'kicks_by_size': {size: quantity}}
    else:
        accessory = Accessories.objects.get(sku=item_id)
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
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
        if quantity > 0:
            bag[item_id]['kicks_by_size'][size] = quantity
        else:
            del bag[item_id]['kicks_by_size'][size]
            if not bag[item_id]['kicks_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

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
            del bag[item_id]['kicks_by_size'][size]
            if not bag[item_id]['kicks_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
