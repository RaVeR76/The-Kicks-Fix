from django.shortcuts import render, get_object_or_404
from .models import Accessories, Type
from kicks.models import Brand, Style

# Create your views here.


def all_accessories(request):
    """ A view to show all accessories, including sorting and search queries """

    accessories = Accessories.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    styles = Style.objects.all()

    if request.GET:
        # Filter ALL Accessories by the selected Type
        if 'type' in request.GET:
            chosen_type = request.GET['type'].split(',')
            accessories = accessories.filter(accessory_type__name__in=chosen_type)

    context = {
        'accessories': accessories,
        'types': types,
        'brands': brands,
        'styles': styles,
    }

    return render(request, 'accessories/accessories.html', context)


def accessory_detail(request, accessories_id):
    """ A view to show one accessory & it's details """

    accessory = get_object_or_404(Accessories, pk=accessories_id)
    types = Type.objects.all()
    brands = Brand.objects.all()
    styles = Style.objects.all()

    context = {
        'accessories': accessory,
        'types': types,
        'brands': brands,
        'styles': styles,
    }

    return render(request, 'accessories/accessory_detail.html', context)
