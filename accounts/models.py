from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.  
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    cost = models.FloatField(max_length=255)

    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(unique=True, max_length=255)
    cnpj = models.CharField(unique=True, max_length=255)
    procuts = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()