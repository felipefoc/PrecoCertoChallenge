from django.urls.base import reverse_lazy
from companies.models import Company
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from challenge1.mixins import AdminStaffRequiredMixin
from companies.models import Company

# Create your views here.
class CompanyCreate(AdminStaffRequiredMixin, CreateView):
    model = Company
    template_name = 'companies/templates/company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('company-list')
    
class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies/templates/company_list.html'
    paginate_by = 10
    

    def get_queryset(self):
        return Company.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = 'company-list'
        return context

class CompanyDelete(DeleteView):
    model = Company
    template_name = 'companies/templates/company_delete.html'
    def get_success_url(self):
        return reverse_lazy('company-list')

class CompanyUpdate(UpdateView):
    model = Company
    fields = ('name' , 'cnpj')
    ordering = 'id'
    pk_url_kwarg = 'pk'
    template_name = 'companies/templates/company_update.html'
    success_url = reverse_lazy('company-list')
