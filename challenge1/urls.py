from django.contrib.auth.views import LogoutView
from accounts.views import Login
from django.urls import path, include
from django.urls.base import reverse_lazy


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('Accounts/', include('accounts.urls')),
    path('Companies/', include('companies.urls')),
    path('Products/', include('products.urls')),
    path('', include('home.urls')),
]
