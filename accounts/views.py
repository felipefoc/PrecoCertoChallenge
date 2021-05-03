from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from accounts.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView, View):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/templates/registration/signup.html'
    

class Login(LoginView):
    success_url = reverse_lazy('home')
    template_name = 'accounts/templates/login/login.html'







