from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic

# Create your views here.
class teste(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home/templates/teste.html'
