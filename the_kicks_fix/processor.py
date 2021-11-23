from django.conf import settings
from home.models import Home
from kicks.models import Brand, Style
from accessories.models import Type
from common.models import Colour


def context(request):
    debug_flag = settings.DEBUG
    return{"debug_flag":debug_flag}


def site_context(request):

    home = Home.objects.get(name='home')
    brands = Brand.objects.all()
    styles = Style.objects.all()
    types = Type.objects.all()
    colours = Colour.objects.all()

    main_slogan = home.main_slogan
    promotion_bar = home.promotion_bar
    main_logo = home.main_logo.url
    toast_logo = home.toast_logo.url
    loader_logo = home.loader_logo.url

    context = {
        'main_slogan': main_slogan,
        'promotion_bar': promotion_bar,
        'main_logo': main_logo,
        'toast_logo': toast_logo,
        'loader_logo': loader_logo,
        'brands': brands,
        'styles': styles,
        'types': types,
        'colours': colours,
    }

    return context
