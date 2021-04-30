from django.urls import path

from .views import Home


urlpatterns = [
    path('<str:name>/', SignUpView.as_view(), name='home'),
]