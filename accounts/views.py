from django.contrib.auth.forms import UserCreationForm
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
    success_url = reverse_lazy('redirect')
    template_name = 'accounts/templates/login/login.html'

    def form_valid(self, form):
        user = form.login(self)
        if user:
            return super(LoginView, self).form_valid(form)

class RedirectView(RedirectView):
    def get_redirect_url(self, param):
        return reverse_lazy('resource-view',
                            kwargs={'param': param},
                            current_app='myapp')