from django.db import models

# Create your models here.
class Produtos(models.Model):
    Nome = models.CharField(max_length=100)
    Preco = models.DecimalField(max_digits=100,decimal_places=2)
    Quantidade = models.IntegerField()


class Tipos_Contas(models.Model):
    choice = (('ADM','Administrador'),('USR','Usuarios'))
    Tipo = models.CharField(choices=choice,max_length=100)


class Usuarios(models.Model):
    choice = (('ADM', 'Administrador'), ('USR', 'Usuarios'))
    Nome = models.CharField(max_length=100)
    Chapa = models.IntegerField()
    Senha = models.CharField(max_length=8)
    Tipo_de_usuario = models.CharField(choices=choice, max_length=100)