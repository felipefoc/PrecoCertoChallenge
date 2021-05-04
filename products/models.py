from django.db import models

# Create your models here.
class Products(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=255)
    price = models.FloatField()
    cost = models.FloatField()
    company = models.ForeignKey("companies.company", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

