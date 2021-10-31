from django.shortcuts import render, get_object_or_404
from .models import Accessories, Type

# Create your views here.


def all_accessories(request):
    """ A view to show all accessories, including sorting and search queries """

    accessories = Accessories.objects.all()
    types = Type.objects.all()

    if request.GET:
        # Filter ALL Accessories by the selected Type
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            accessories = accessories.filter(accessory_type__name__in=types)

    context = {
        'accessories': accessories,
        'types': types,
    }

    return render(request, 'accessories/accessories.html', context)


def accessory_detail(request, accessories_id):
    """ A view to show one accessory & it's details """

    accessory = get_object_or_404(Accessories, pk=accessories_id)

    context = {
        'accessories': accessory,
    }

    return render(request, 'accessories/accessory_detail.html', context)
