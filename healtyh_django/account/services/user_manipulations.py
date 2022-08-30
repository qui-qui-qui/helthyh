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

def authenticate_user(user_form: UserLoginForm)->User:
    cd = user_form.cleaned_data
    return authenticate(username=cd['username'], password=cd['password'])


def edit_user(user_form:UserEditForm, account_form:  AccountEditForm)->(UserEditForm,AccountEditForm):
    if user_form.is_valid() and account_form.is_valid():
        new_user=user_form.save()
        new_account=account_form.save()
        return new_user,new_account

