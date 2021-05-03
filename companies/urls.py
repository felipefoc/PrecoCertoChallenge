from django.urls import path
from .views import CompanyCreate


urlpatterns = [
    path('NewCompany/', CompanyCreate.as_view(), name='company_create'),
]