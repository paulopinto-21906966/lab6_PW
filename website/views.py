#  hello/views.py
from datetime import datetime
from random import randint

from django.shortcuts import render
from website.funs import *

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Tarefa
from .forms import TarefaForm


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


def admin_tarefa_view(request):
    return render(request, '/admin.html')


def tarefas_tarefa_view(request):
    context = {
        'tarefas': Tarefa.objects.all()
    }
    return render(request, 'website/tarefas.html', context)


def nova_tarefa_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form}

    return render(request, 'website/nova.html', context)


def edita_tarefa_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:home'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'website/edita.html', context)


def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('website:home'))
