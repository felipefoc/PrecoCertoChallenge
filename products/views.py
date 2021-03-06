from products.models import Products
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from challenge1.mixins import AdminStaffRequiredMixin

# Create your views here.
class ProductCreate(AdminStaffRequiredMixin, CreateView):
    model = Products
    template_name = 'products/templates/products_create.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class ProductList(ListView):
    model = Products
    paginate_by = 5
    template_name = 'products/templates/products_list.html'


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Products.objects.all()
        else:
            return Products.objects.filter(company=self.request.user.company)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = 'product-list'
        return context

class ProductUpdate(AdminStaffRequiredMixin, UpdateView):
    model = Products
    fields = ('name' , 'price', 'cost', 'company')
    pk_url_kwarg = 'pk'
    template_name = 'products/templates/products_update.html'
    success_url = reverse_lazy('product-list')


class ProductDelete(AdminStaffRequiredMixin, DeleteView):
    model = Products
    template_name = 'products/templates/products_delete.html'
    def get_success_url(self):
        return reverse_lazy('products-list')

