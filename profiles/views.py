from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import UserProfileForm
from .forms import UserTestProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

   #first_name = UserProfile.user.first_name

    #print(first_name)
   # print(last_name)

    if request.method == 'POST':
        form = UserTestProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserTestProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True, # Don't forget to delete this from toast success if unused
       # 'orders': orders,
    }

    return render(request, template, context)


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
