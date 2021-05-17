from django.urls import path
from django.shortcuts import render
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('outro/<str:name>', views.outro_page_view, name='outro'),
    path('about', views.about_page_view, name='about'),
]
