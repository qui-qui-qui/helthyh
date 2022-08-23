from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', register_user_view, name='register'),
]