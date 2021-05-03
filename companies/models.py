from products.models import Products
from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(unique=True, max_length=255)
    cnpj = models.CharField(unique=True, max_length=18)

    def __str__(self):
        return self.name

