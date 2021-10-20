from django.shortcuts import render
from .models import Kicks

# Create your views here.


def all_kicks(request):
    """ A view to show all kicks, including sorting and search queries """

    kicks = Kicks.objects.all()

    context = {
        'kicks': kicks,
    }

    return render(request, 'kicks/kicks.html', context)
