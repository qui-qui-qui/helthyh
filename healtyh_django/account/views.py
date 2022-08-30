from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from .forms import  UserLoginForm, UserRegistrationForm, UserEditForm, AccountEditForm
from .services.user_manipulations import register_user, edit_user,login_user


def register_user_view(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = register_user(user_form)
            login_user(user_form.cleaned_data['username'],user_form.cleaned_data['password'],request)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def login_user_view(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            if login_user(user_form.cleaned_data['username'],user_form.cleaned_data['password'],request):
                return redirect('main_menu')                
            else:
                error_msg="Your username and password didn't match. Please try again."
            return render(request, 'account/login.html', {'error_msg':error_msg,'form': user_form})
    else:
        user_form = UserLoginForm()
    return render(request, 'account/login.html', {'form': user_form})

def logout_user_view(request):
    logout(request)
    return redirect('login')

@login_required
def edit_user_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        account_form = AccountEditForm(instance=request.user.account, data=request.POST, files=request.FILES)
        new_user_form,new_account_form=edit_user(user_form,account_form)
        return render(request,
            'account/edit.html',
            {'user_form': user_form,
            'account_form': account_form})
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = AccountEditForm(instance=request.user.account)
        return render(request,
                      'account/edit.html',
                      {'user_form': user_form,
                       'account_form': profile_form})