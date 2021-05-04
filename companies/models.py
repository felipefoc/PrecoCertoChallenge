from products.models import Products
from companies.validations import validate_cnpj
from django.db import models

# Create your models here.
class Company(models.Model):
    class Meta:
        ordering = ['-id']

    name = models.CharField(unique=True, max_length=255)
    cnpj = models.CharField(unique=True, max_length=18)

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        validate_cnpj(self.cnpj)
        super(Company, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Company, self).save(*args, **kwargs)



