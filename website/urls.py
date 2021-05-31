from django.urls import path
from django.shortcuts import render
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('outro/<str:number>', views.outro_page_view, name='outro'),
    path('about', views.about_page_view, name='about'),
    path('admin', views.admin_tarefa_view, name='admin'),
    path('tarefas/', views.tarefas_tarefa_view, name='tarefas')
]
