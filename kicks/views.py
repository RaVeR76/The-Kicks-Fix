from django.shortcuts import render, get_object_or_404
from .models import Kicks

# Create your views here.


def all_kicks(request):
    """ A view to show all kicks, including sorting and search queries """

    kicks = Kicks.objects.all()

    context = {
        'kicks': kicks,
    }

    return render(request, 'kicks/kicks.html', context)


def kicks_detail(request, kicks_id):
    """ A view to show one pair of kicks & it's details """

    kicks = get_object_or_404(Kicks, pk=kicks_id)

    context = {
        'kicks': kicks,
    }

    return render(request, 'kicks/kicks_detail.html', context)
