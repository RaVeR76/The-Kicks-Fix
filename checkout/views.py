from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('kicks'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JajHVAzVUHq5fIcar41NgpGugMrUZdyZhToVmy8UnfEN07q6HkOSwK0Y0PQ6zHZ1B8fmwM4sKoIRYKmHggnZvEX00dwJ61vA2',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
