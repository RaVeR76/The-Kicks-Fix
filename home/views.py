from django.shortcuts import render
from .models import Home
from kicks.models import Brand, Style
from accessories.models import Type

# Create your views here.


def index(request):
    """ A view to return the index page """
    """ Pass Brands, Style & Type into home.html for navbar usage """

    home = Home.objects.all()
    brands = Brand.objects.all()
    styles = Style.objects.all()
    types = Type.objects.all()

   # main_slogan = Home.objects.get(main_slogan__exact='main_slogan')

    context = {
        'home': home,
        'brands': brands,
        'styles': styles,
        'types': types,
    }

    return render(request, 'home/index.html', context)
