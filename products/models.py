from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=999999, decimal_places=2)
    cost = models.DecimalField(max_digits=999999, decimal_places=2)
    company = models.ForeignKey("companies.company", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

