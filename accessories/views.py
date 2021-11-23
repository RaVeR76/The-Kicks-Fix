from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages

from .models import Accessories, Type
from common.models import Category
from .forms import AccessoriesForm

# Create your views here.


def all_accessories(request):
    """ A view to show all accessories, including sorting and search queries """

    accessories = Accessories.objects.all()
    types = Type.objects.all()
    sort = None
    direction = None
    accessories_title = 'All Accessories'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                accessories = accessories.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            accessories = accessories.order_by(sortkey)

    if request.GET:
        # Filter ALL Accessories by the selected Category
        if 'category' in request.GET:
            chosen_category = request.GET['category'].split(',')
            accessories = accessories.filter(category__name__in=chosen_category)
            chosen_category = Category.objects.filter(name__in=chosen_category).first()
            accessories_title = f'{chosen_category.friendly_name} Accessories'

        # Filter ALL Accessories by the selected Type
        if 'type' in request.GET:
            chosen_type = request.GET['type'].split(',')
            accessories = accessories.filter(type__name__in=chosen_type)
            chosen_type = Type.objects.filter(name__in=chosen_type).first()
            accessories_title = f'{chosen_type.friendly_name} Accessories'

    current_sorting = f'{sort}_{direction}'

    context = {
        'accessories_title': accessories_title,
        'accessories': accessories,
        'current_sorting': current_sorting,
    }

    return render(request, 'accessories/accessories.html', context)


def accessory_detail(request, accessories_id):
    """ A view to show one accessory & it's details """

    accessory = get_object_or_404(Accessories, pk=accessories_id)

    context = {
        'accessories': accessory,
    }

    return render(request, 'accessories/accessory_detail.html', context)


def add_accessory(request):
    """" Add a new Accessory to the store """

    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            accessory = form.save()
            messages.success(request, 'Successfully added the Accessory !')
            return redirect(reverse('accessory_detail', args=[accessory.id]))
        else:
            messages.error(request, 'Failed to add the Accessory. Please ensure the form is valid.')
    else:
        form = AccessoriesForm()

    template = 'accessories/add_accessory.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_accessory(request, accessories_id):
    """" Edit an Accessory to the store """

    accessory = get_object_or_404(Accessories, pk=accessories_id)

    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES, instance=accessory)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Accessory !')
            return redirect(reverse('accessory_detail', args=[accessory.id]))
        else:
            messages.error(request, 'Failed to add the Accessory. Please ensure the form is valid.')
    else:
        form = AccessoriesForm(instance=accessory)
        messages.info(request, f'You are editing {accessory.name}')

    template = 'accessories/edit_accessory.html'
    context = {
        'form': form,
        'accessories': accessory,
    }

    return render(request, template, context)


def delete_accessory(request, accessories_id):
    """ Delete Accessory from the store """

    accessory = get_object_or_404(Accessories, pk=accessories_id)
    accessory.delete()
    messages.success(request, 'Accessory deleted !')
    return redirect(reverse('accessories'))
