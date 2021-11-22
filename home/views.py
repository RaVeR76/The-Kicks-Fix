from django.shortcuts import render
from kicks.models import Brand, Style
from accessories.models import Type
from common.models import Colour

# Create your views here.


def index(request):
    """ A view to return the index page """
    """ Pass Brands, Style & Type into home.html for navbar usage """

    brands = Brand.objects.all()
    styles = Style.objects.all()
    types = Type.objects.all()
    colours = Colour.objects.all()

    context = {
        'brands': brands,
        'styles': styles,
        'types': types,
        'colours': colours,
    }

    return render(request, 'home/index.html', context)
