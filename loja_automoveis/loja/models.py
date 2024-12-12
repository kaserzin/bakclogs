from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ano = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    carros = models.ManyToManyField(Carro)

    def __str__(self):
        return f"Venda {self.id} - {self.data}"

class Manutencao(models.Model):
    data = models.CharField(max_length=100)
    descricao = models.TextField()
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    def __str__(self):
        return f"Manutenção {self.carro} - {self.data}"
