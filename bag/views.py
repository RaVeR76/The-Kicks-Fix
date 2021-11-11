from django.shortcuts import render, redirect

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
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
