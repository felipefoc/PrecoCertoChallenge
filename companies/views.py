from django.urls.base import reverse_lazy
from companies.models import Company
from django.views.generic import CreateView

# Create your views here.
class CompanyCreate(CreateView):
    model = Company
    template_name = 'companies/templates/company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')