from django.shortcuts import render
# Create your views here.


def main_menu(request):
    context = {}
    return render(request, 'main_menu/index.html', context)
