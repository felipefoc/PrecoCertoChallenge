from django.urls import path
from companies.views import CompanyCreate, CompanyList, CompanyDelete, CompanyUpdate


urlpatterns = [
    path('Create/', CompanyCreate.as_view(), name='company-create'),
    path('', CompanyList.as_view(), name='company-list'),
    path('Delete/<pk>', CompanyDelete.as_view(), name='company-delete'),
    path('Update/<pk>', CompanyUpdate.as_view(), name='company-update'),

]