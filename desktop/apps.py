from django.apps import AppConfig
from .models import AdvUser


class DesktopConfig(AppConfig):
    name = 'desktop'
    verbose_name = 'Доска объявлений'
