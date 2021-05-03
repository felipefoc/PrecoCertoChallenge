from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls.base import reverse_lazy


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
     def test_func(self):
          return self.request.user.is_superuser or self.request.user.is_staff

     