from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Kicks
from common.models import Category

# Create your views here.


def all_kicks(request):
    """ A view to show all kicks, including sorting and search queries """

    kicks = Kicks.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            kicks = kicks.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            kicks = kicks.filter(queries)

    context = {
        'kicks': kicks,
        'search_word': query,
       # 'chosen_categories': categories,
    }

    return render(request, 'kicks/kicks.html', context)


def kicks_detail(request, kicks_id):
    """ A view to show one pair of kicks & it's details """

    pair_of_kicks = get_object_or_404(Kicks, pk=kicks_id)

    context = {
        'kicks': pair_of_kicks,
    }

    return render(request, 'kicks/kicks_detail.html', context)
