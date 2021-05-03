from django.urls.base import reverse_lazy
from companies.models import Company
from django.views.generic import CreateView, ListView

# Create your views here.
class CompanyCreate(CreateView):
    model = Company
    template_name = 'companies/templates/company_create.html'
    fields = '__all__'
    success_url = reverse_lazy('login')
    
class CompanyList(ListView):
    model = Company
    template_name = 'companies/templates/company_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Company.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = 'company-list'
        return context
