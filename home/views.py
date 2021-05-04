from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

# Create your views here.
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'home/templates/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = 'home'
        return context
