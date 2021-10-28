from django.shortcuts import render
from .models import Accessories

# Create your views here.


def all_accessories(request):
    """ A view to show all kaccessories, including sorting and search queries """

    accessories = Accessories.objects.all()

    context = {
        'accessories': accessories,
    }

    return render(request, 'accessories/accessories.html', context)
