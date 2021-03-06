"""
This module will render ALL Kicks requirements
diplaying, details, filtering, Admin ADD,
Admin Edit and Admin Delete
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from common.models import Category, Sex, Size, Colour
from .models import Kicks, Brand, Style
from .forms import KicksForm

# Create your views here.


def all_kicks(request):
    """ A view to show all kicks, including sorting and search queries """

    kicks = Kicks.objects.all()
    query = None
    sort = None
    direction = None
    kicks_title = 'All Kicks'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                kicks = kicks.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            kicks = kicks.order_by(sortkey)

        # Filter ALL Kicks by the selected Category
        if 'category' in request.GET:
            chosen_category = request.GET['category'].split(',')
            kicks = kicks.filter(category__name__in=chosen_category)
            chosen_category = Category.objects.filter(
                name__in=chosen_category).first()
            kicks_title = f'All {chosen_category.friendly_name} Kicks'

            # Filter Navbar Sex from the Category filtered Kicks above
            if 'sex' in request.GET:
                chosen_sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=chosen_sex)
                chosen_sex = Sex.objects.filter(name__in=chosen_sex).first()
                kicks_title = f"{chosen_sex.friendly_name}'s"\
                              f" {chosen_category.friendly_name} Kicks"

        # Filter ALL Kicks by the selected Brand
        if 'brand' in request.GET:
            chosen_brand = request.GET['brand'].split(',')
            kicks = kicks.filter(brand__name__in=chosen_brand)
            chosen_brand = Brand.objects.filter(name__in=chosen_brand).first()
            kicks_title = f"All {chosen_brand.friendly_name} Kicks"
            # Filter Navbar Sex from the Brand filtered Kicks above
            if 'sex' in request.GET:
                chosen_sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=chosen_sex)
                chosen_sex = Sex.objects.filter(name__in=chosen_sex).first()
                kicks_title = f"{chosen_sex.friendly_name}'s"\
                              f" {chosen_brand.friendly_name} Kicks"

        # Filter ALL Kicks by the selected Style
        if 'style' in request.GET:
            chosen_style = request.GET['style'].split(',')
            kicks = kicks.filter(style__name__in=chosen_style)
            chosen_style = Style.objects.filter(name__in=chosen_style).first()
            kicks_title = f"All {chosen_style.friendly_name} Kicks"
            # Filter Navbar Sex from the Style filtered Kicks above
            if 'sex' in request.GET:
                chosen_sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=chosen_sex)
                chosen_sex = Sex.objects.filter(name__in=chosen_sex).first()
                kicks_title = f"{chosen_sex.friendly_name}'s"\
                              f" {chosen_style.friendly_name} Kicks"

        # Filter ALL Kicks by the selected Colour
        if 'colour' in request.GET:
            chosen_colour = request.GET['colour'].split(',')
            kicks = kicks.filter(colour__name__in=chosen_colour)
            chosen_colour = Colour.objects.filter(
                name__in=chosen_colour).first()
            kicks_title = f"All {chosen_colour.friendly_name} Kicks"
            # Filter Navbar Sex from the Colour filtered Kicks above
            if 'sex' in request.GET:
                chosen_sex = request.GET['sex'].split(',')
                kicks = kicks.filter(sex__name__in=chosen_sex)
                chosen_sex = Sex.objects.filter(name__in=chosen_sex).first()
                kicks_title = f"{chosen_sex.friendly_name}'s"\
                              f" {chosen_colour.friendly_name} Kicks"

        # Filter ALL Kicks by Sex only
        if 'category' not in request.GET:
            pass
            if 'brand' not in request.GET:
                pass
                if 'style' not in request.GET:
                    pass
                    if 'colour' not in request.GET:
                        pass
# Needed all the PASSES so it would just display SEX ONLY with Title too
                        if 'sex' in request.GET:
                            chosen_sex = request.GET['sex'].split(',')
                            kicks = kicks.filter(sex__name__in=chosen_sex)
                            chosen_sex = Sex.objects.filter(
                                name__in=chosen_sex).first()
                            kicks_title = f"All"\
                                f" {chosen_sex.friendly_name}'s Kicks"

        # Filter ALL Kicks by name or description using tye search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter"
                                        " any search criteria!")
                return redirect(reverse('kicks'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            kicks = kicks.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'kicks_title': kicks_title,
        'kicks': kicks,
        'search_word': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'kicks/kicks.html', context)


# Get selected pair of Kicks for displaying more info
def kicks_detail(request, kicks_id):
    """ A view to show one pair of kicks & it's details """

    pair_of_kicks = get_object_or_404(Kicks, pk=kicks_id)

    kids_sizes = Size.objects.get(name='kids_sizes')
    kids_sizes_uk = kids_sizes.size.get("uk")
    kids_sizes_eu = kids_sizes.size.get("eu")
    kids_sizes_us = kids_sizes.size.get("us")

    women_sizes = Size.objects.get(name='women_sizes')
    women_sizes_uk = women_sizes.size.get("uk")
    women_sizes_eu = women_sizes.size.get("eu")
    women_sizes_us = women_sizes.size.get("us")

    men_sizes = Size.objects.get(name='men_sizes')
    men_sizes_uk = men_sizes.size.get("uk")
    men_sizes_eu = men_sizes.size.get("eu")
    men_sizes_us = men_sizes.size.get("us")

    context = {
        'kicks': pair_of_kicks,
        'kids_sizes_uk': kids_sizes_uk,
        'kids_sizes_eu': kids_sizes_eu,
        'kids_sizes_us': kids_sizes_us,
        'women_sizes_uk': women_sizes_uk,
        'women_sizes_eu': women_sizes_eu,
        'women_sizes_us': women_sizes_us,
        'men_sizes_uk': men_sizes_uk,
        'men_sizes_eu': men_sizes_eu,
        'men_sizes_us': men_sizes_us,
    }

    return render(request, 'kicks/kicks_detail.html', context)


@login_required
def add_kicks(request):
    """" Add new Kicks to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = KicksForm(request.POST, request.FILES)
        if form.is_valid():
            kicks = form.save()
            messages.success(request, 'Successfully added the Kicks !')
            return redirect(reverse('kicks_detail', args=[kicks.id]))
        else:
            messages.error(request, 'Failed to add the Kicks.'
                                    ' Please ensure the form is valid.')
    else:
        form = KicksForm()

    template = 'kicks/add_kicks.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_kicks(request, kicks_id):
    """ Edit some Kicks within the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    kicks = get_object_or_404(Kicks, pk=kicks_id)

    if request.method == 'POST':
        form = KicksForm(request.POST, request.FILES, instance=kicks)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the Kicks !')
            return redirect(reverse('kicks_detail', args=[kicks.id]))
        else:
            messages.error(request, 'Failed to update Kicks.'
                                    ' Please ensure the form is valid')
    else:
        form = KicksForm(instance=kicks)
        messages.info(request, f'You are editing {kicks.name}')

    template = 'kicks/edit_kicks.html'
    context = {
        'form': form,
        'kicks': kicks,
    }

    return render(request, template, context)


@login_required
def delete_kicks(request, kicks_id):
    """ Delete Kicks from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store admin can do that.')
        return redirect(reverse('home'))

    kicks = get_object_or_404(Kicks, pk=kicks_id)
    kicks.delete()
    messages.success(request, 'Kicks deleted !')
    return redirect(reverse('kicks'))
