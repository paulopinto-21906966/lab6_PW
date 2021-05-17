#  hello/views.py
from datetime import datetime

from django.shortcuts import render


def home_page_view(request):
    context = {
        'data': datetime.now()
    }
    return render(request, '../templates/website/home.html', context)


def about_page_view(request):
    return render(request, 'website/about.html')


def outro_page_view(request, name):
    context = {
        'name': name
    }

    # TODO: ALGORITMO get next fibonacci??


    return render(request, 'website/outro.html/', context)
