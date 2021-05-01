from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from accounts.forms import LoginForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/templates/registration/signup.html'

class LoginView(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/templates/login/login.html'

    def form_valid(self, form):
        user = form.login(self)
        if user:
            return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

