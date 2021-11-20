from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserOrdersProfile
from .forms import UserOrdersProfileForm

from checkout.models import Order


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
    profile_address = get_object_or_404(UserOrdersProfile, user=request.user)

    if request.method == 'POST':
        form = UserOrdersProfileForm(request.POST, instance=profile_address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery Info updated successfully')

    form = UserOrdersProfileForm(instance=profile_address)
    orders = profile_address.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'form': form,
        'orders': orders,
        'on_order_history_page': True,
    }

    return render(request, template, context)


def previous_orders(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_order_history': True,
    }

    return render(request, template, context)
