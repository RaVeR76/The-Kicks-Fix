from django.shortcuts import render


# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact_us(request):
    """ A view to return the contact us page """

    return render(request, 'home/contact_us.html')


def kicks_club(request):
    """ A view to return the Kicks Club page """

    return render(request, 'home/kicks_club.html')
