from django.shortcuts import render
from django. views. generic import TemplateView 

class HomeView(TemplateView) : 
    """Docstring for HomeView. """

    template_name = 'home.html'
