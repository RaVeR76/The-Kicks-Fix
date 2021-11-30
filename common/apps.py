""" Common App Configuration """
from django.apps import AppConfig


class CommonConfig(AppConfig):
    """ Common App Name """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
