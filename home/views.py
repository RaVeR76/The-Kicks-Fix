"""
This module will render Home,
Contact Us and KFC pages
"""
from django.shortcuts import render


def index(request):
    """ A view to return the home page """

    return render(request, 'home/index.html')


def contact_us(request):
    """ A view to return the contact us page """

    return render(request, 'home/contact_us.html')


def kicks_club(request):
    """ A view to return the kicks club page """

    return render(request, 'home/kicks_club.html')
