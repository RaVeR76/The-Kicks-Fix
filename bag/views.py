from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """" My Bag view see the user can see their shopping bag so far """

    return render(request, 'bag/bag.html')
