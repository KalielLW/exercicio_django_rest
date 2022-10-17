from django.db import models

class Revendedor(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    
class Marca(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=250)

class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Carro(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.FloatField(max_length=10)
    ano = models.IntegerField()
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    revendedor = models.ForeignKey(Revendedor, on_delete=models.CASCADE, default=None, null=True)