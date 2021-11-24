from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from .forms import UserTestProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile info """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserTestProfileForm(instance=profile)

    user_birthdate = '15/03/1976' # For display purposes only

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'user_birthdate': user_birthdate,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    """ Display the user's delivery details & order history. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Delivery Info updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

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
