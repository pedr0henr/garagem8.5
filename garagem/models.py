from django.db import models

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cor (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField( default = 0,null=True, blank=True, max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}, {self.cor}"