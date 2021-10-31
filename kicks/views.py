from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Kicks, Brand, Style
from common.models import Category, Sex
from accessories.models import Type

# Create your views here.


def all_kicks(request):
    """ A view to show all kicks, including sorting and search queries """

    kicks = Kicks.objects.all()
    brands = Brand.objects.all()
    styles = Style.objects.all()
    types = Type.objects.all()
    query = None
    category = None
    sex = None

    if request.GET:
        # Filter ALL Kicks by the selected Category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            kicks = kicks.filter(category__name__in=categories)
        #    categories = Category.objects.filter(name__in=categories)

            # Filter Navbar Sex from the Category filtered Kicks above
            if 'sex' in request.GET:
                sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=sex)

        # Filter ALL Kicks by Brand from the selected navbar Brands submenu
        if 'brand' in request.GET:
            chosen_brand = request.GET['brand'].split(',')
            kicks = kicks.filter(brand__name__in=chosen_brand)

            # Filter Navbar Sex from the Brand filtered Kicks above
            if 'sex' in request.GET:
                sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=sex)

        # Filter ALL Kicks by the Style from the selected navbar Styles submenu
        if 'style' in request.GET:
            chosen_style = request.GET['style'].split(',')
            kicks = kicks.filter(style__name__in=chosen_style)

            # Filter Navbar Sex from the Style filtered Kicks above
            if 'sex' in request.GET:
                sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=sex)

        # Filter ALL Kicks by selected Sex
        if 'sex' in request.GET:
            sex = request.GET['sex'].split(',')
            kicks = kicks.filter(sex__name__in=sex)

        # Filter ALL Kicks by name or description using tye search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('kicks'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            kicks = kicks.filter(queries)

    context = {
        'kicks': kicks,
        'search_word': query,
        'brands': brands,
        'styles': styles,
        'types': types,
      #  'chosen_categories': categories,
    }

    return render(request, 'kicks/kicks.html', context)

# Get selected pair of Kicks for displaying more info
def kicks_detail(request, kicks_id):
    """ A view to show one pair of kicks & it's details """

    pair_of_kicks = get_object_or_404(Kicks, pk=kicks_id)
    brands = Brand.objects.all()
    styles = Style.objects.all()
    types = Type.objects.all()

    context = {
        'kicks': pair_of_kicks,
        'brands': brands,
        'styles': styles,
        'types': types,
    }

    return render(request, 'kicks/kicks_detail.html', context)
