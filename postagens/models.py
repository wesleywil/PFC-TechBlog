from tabnanny import verbose
from django.db import models
from contas.models import Perfil

class Postagem(models.Model):
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_adicao = models.DateField(auto_now_add=True)
    categorias = models.ManyToManyField("Categoria", blank=True)

    class Meta:
        verbose_name = "postagem"
        verbose_name_plural = "postagens"

    def __str__(self):
        return self.titulo
    

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

