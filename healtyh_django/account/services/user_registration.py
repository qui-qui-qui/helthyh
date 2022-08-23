from django.contrib.auth.models import User
from ..models import Account
from ..forms import UserRegistrationForm


def register_user(user_form: UserRegistrationForm)->User:

    new_user = user_form.save(commit=False)

    new_user.set_password(user_form.cleaned_data['password'])

    new_user.save()

    return new_user
