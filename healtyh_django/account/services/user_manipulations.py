from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ..models import Account
from ..forms import  UserLoginForm, UserRegistrationForm, UserEditForm, AccountEditForm


def register_user(user_form: UserRegistrationForm)->User:
    new_user = user_form.save(commit=False)
    new_user.set_password(user_form.cleaned_data['password'])
    new_user.save()
    Account.objects.create(user=new_user)
    return new_user

def _authenticate_user(username:str, password:str)->User:
    return authenticate(username=username, password=password)

def login_user(username:str,password:str, request)->bool:
    user = _authenticate_user(username,password)
    if user is not None:
        login(request, user) 
        return True
    return False         
                    

def edit_user(user_form:UserEditForm, account_form:  AccountEditForm)->(UserEditForm,AccountEditForm):
    if user_form.is_valid() and account_form.is_valid():
        new_user=user_form.save()
        new_account=account_form.save()
        return new_user,new_account

