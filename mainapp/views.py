from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class mainappView(TemplateView):
    template_name = 'home.html'

class aboutView(TemplateView):
    template_name = 'about.html'

class cantactView(TemplateView):
    template_name = 'cantact.html'

class blogView(TemplateView):
    template_name = 'blog.html'