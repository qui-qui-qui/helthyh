from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main_menu, name='main_menu'),

    #path('', Documents.as_view(), name='catalog'),
]