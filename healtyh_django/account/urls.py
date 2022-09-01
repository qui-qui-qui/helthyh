from django.urls import path, re_path  
from .views import register_user_view, edit_user_view,login_user_view,logout_user_view

urlpatterns = [
    path('register/', register_user_view, name='register'),
    path('edit/',edit_user_view,name='edit'),
    path('login/', login_user_view, name='login'),
    path('logout/', logout_user_view, name='logout'),
]