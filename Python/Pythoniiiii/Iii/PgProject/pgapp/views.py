from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HiPgView(TemplateView):
    template_name = 'hi.html'
class AboutView(TemplateView):
    template_name = 'iii.html'
