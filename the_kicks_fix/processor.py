from django.conf import settings
from home.models import Home


def context(request):
    debug_flag = settings.DEBUG
    return{"debug_flag":debug_flag}


def site_context(request):

    home = Home.objects.get(name='home')
    main_slogan = home.main_slogan
    logo = home.logo.url

    context = {
        'main_slogan': main_slogan,
        'logo': logo,
    }

    return context
