# encoding: utf-8

from django.shortcuts import render_to_response
from django.conf import settings
from django.views.generic import DetailView, TemplateView, CreateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

class Home(TemplateView):
    template_name = 'index.html'

    
    