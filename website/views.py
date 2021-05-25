#  hello/views.py
from datetime import datetime
from random import randint

# import numpy as np
from django.shortcuts import render
from website.funs import *


def home_page_view(request):
    context = {
        'data': datetime.now()
    }
    return render(request, '../templates/website/home.html', context)


def about_page_view(request):
    return render(request, 'website/about.html')


def outro_page_view(request, number):
    lista = [randint(0, 100), randint(100, 1000)]

    # r = np.random.choice(lista, p=[0.8, 0.2])
    r = lista[1 if randint(0, 10) < 8 else 0]
    number = r if int(number) == 0 else int(number)

    fibonacci = nextFib(number)

    context = {
        'number': number,
        'fib': fibonacci
    }

    return render(request, 'website/outro.html/', context)
