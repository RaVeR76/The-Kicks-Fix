from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserOrdersProfile
from .forms import UserOrdersProfileForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserOrdersProfile, user=request.user)

    form = UserOrdersProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request):
    """ Display the user's delivery details & order history. """
    delivery_address = get_object_or_404(UserOrdersProfile, user=request.user)

    if request.method == 'POST':
        form = UserOrdersProfileForm(request.POST, instance=delivery_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery Info updated successfully')

    form = UserOrdersProfileForm(instance=delivery_address)
    orders = delivery_address.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'form': form,
        'orders': orders,
        'on_order_history_page': True,
    }

    return render(request, template, context)
