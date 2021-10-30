from django.shortcuts import render
from kicks.models import Brand

# Create your views here.


def index(request):
    """ A view to return the index page """
    """ Pass Brands into home.html for navbar usage """

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }

    return render(request, 'home/index.html', context)
