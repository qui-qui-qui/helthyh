from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def main_menu(request):
    context = {}
    return render(request, 'main_menu/index.html', context)
