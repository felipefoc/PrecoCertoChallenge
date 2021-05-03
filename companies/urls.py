from django.urls import path
from .views import CompanyCreate, CompanyList


urlpatterns = [
    path('AddCompany/', CompanyCreate.as_view(), name='company-create'),
    path('', CompanyList.as_view(), name='company-list'),
]