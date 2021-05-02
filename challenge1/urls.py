from django.contrib import admin
from django.contrib.auth.views import LogoutView
from accounts.views import Login
from django.urls import path, include
from django.urls.base import reverse_lazy


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
]
