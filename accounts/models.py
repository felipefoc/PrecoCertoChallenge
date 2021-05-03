from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.     
class CustomUser(AbstractUser):
    company = models.ForeignKey("companies.company",on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username