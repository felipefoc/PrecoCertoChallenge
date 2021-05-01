from django.urls import path

from .views import teste


urlpatterns = [
    path('', teste.as_view(), name='home'),
]