from django.shortcuts import render, get_object_or_404
from .models import Accessories

# Create your views here.


def all_accessories(request):
    """ A view to show all accessories, including sorting and search queries """

    accessories = Accessories.objects.all()

    context = {
        'accessories': accessories,
    }

    return render(request, 'accessories/accessories.html', context)


def accessory_detail(request, accessories_id):
    """ A view to show one accessory & it's details """

    accessory = get_object_or_404(Accessories, pk=accessories_id)

    context = {
        'accessories': accessory,
    }

    return render(request, 'accessories/accessory_detail.html', context)
