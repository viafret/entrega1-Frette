from django.apps import AppConfig
from django.contrib import admin
#from .models import *


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App1'

#admin.site.register(Familia)