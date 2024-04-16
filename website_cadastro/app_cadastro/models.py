from django.db import models

# Create your models here.
class Pessoa(models.Model):
    PAISES = [
        ('Estados Unidos', 'Estados Unidos'),
        ('Canadá', 'Canadá'),
        ('Reino Unido', 'Reino Unido'),
        ('França', 'França'),
        ('Alemanha', 'Alemanha'),
        ('Japão', 'Japão'),
        ('China', 'China'),
        ('Índia', 'Índia'),
        ('Austrália', 'Austrália'),
    ]

    nome = models.CharField(max_length=125)
    email = models.CharField(max_length=155, default="N/A")
    pais = models.CharField(max_length=60, choices=PAISES)
    nascimento = models.DateField()
    criado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado']

    def __str__(self):
        return self.nome
    



