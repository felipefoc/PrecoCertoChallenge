from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import UserForm, ProfileForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = [ProfileForm, UserForm]
    success_url = reverse_lazy('login')
    template_name = 'accounts/templates/registration/signup.html'

class Login(LoginView):
    success_url = reverse_lazy('home')
    template_name = 'accounts/templates/login/login.html'



