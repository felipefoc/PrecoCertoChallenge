
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    empresa = models.ForeignKey("accounts.Empresa", on_delete=models.CASCADE)  

    def __str__(self):
        return self.usuario
     

class Empresa(models.Model):
    nome = models.CharField(unique=True, max_length=255)
    cnpj = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preço = models.FloatField(max_length=255)
    custo = models.FloatField(max_length=255)

    def __str__(self):
        return self.nome
    
