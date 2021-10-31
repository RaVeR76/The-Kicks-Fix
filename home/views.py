from django.shortcuts import render
from kicks.models import Brand, Style

# Create your views here.


def index(request):
    """ A view to return the index page """
    """ Pass Brands into home.html for navbar usage """

    brands = Brand.objects.all()
    styles = Style.objects.all()

    context = {
        'brands': brands,
        'styles': styles,
    }

    return render(request, 'home/index.html', context)
