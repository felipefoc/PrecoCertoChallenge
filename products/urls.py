from django.urls import path

from products.views import ProductCreate, ProductUpdate, ProductList, ProductDelete


urlpatterns = [
    path('Create/', ProductCreate.as_view(), name='product-create'),
    path('Update/<pk>', ProductUpdate.as_view(), name='product-update'),
    path('', ProductList.as_view(), name='product-list'),
    path('Delete/<pk>', ProductDelete.as_view(), name='product-delete')
]