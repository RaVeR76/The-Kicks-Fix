from django.shortcuts import render, get_object_or_404
from .models import Accessories, Type
from kicks.models import Brand, Style
from common.models import Category

# Create your views here.


def all_accessories(request):
    """ A view to show all accessories, including sorting and search queries """

    accessories = Accessories.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    styles = Style.objects.all()
    accessories_title = 'All Accessories'

    if request.GET:
        # Filter ALL Accessories by the selected Category
        if 'category' in request.GET:
            chosen_category = request.GET['category'].split(',')
            accessories = accessories.filter(category__name__in=chosen_category)
            chosen_category = Category.objects.filter(name__in=chosen_category).first()
            accessories_title = f'All {chosen_category.friendly_name} Accessories'

        # Filter ALL Accessories by the selected Type
        if 'type' in request.GET:
            chosen_type = request.GET['type'].split(',')
            accessories = accessories.filter(accessory_type__name__in=chosen_type)
            chosen_type = Type.objects.filter(name__in=chosen_type).first()
            accessories_title = f'All {chosen_type.friendly_name} Accessories'

    context = {
        'accessories_title': accessories_title,
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
