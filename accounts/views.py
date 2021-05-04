from django.contrib.auth.views import LoginView
from django.views.generic.base import View
from accounts.forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import generic
from challenge1.mixins import AdminStaffRequiredMixin


class SignUpView(AdminStaffRequiredMixin, generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/templates/registration/signup.html'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=401)

    
class Login(LoginView):
    success_url = reverse_lazy('home')
    template_name = 'accounts/templates/login/login.html'

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=401)






