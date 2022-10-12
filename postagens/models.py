from django.db import models
from contas.models import Usuario

from PIL import Image
from djrichtextfield.models import RichTextField

class Postagem(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="postagens/", default="postagens/predefinido/default.png")
    titulo = models.CharField(max_length=100)
    texto = RichTextField()
    data_adicao = models.DateField(auto_now_add=True)
    categorias = models.ManyToManyField("Categoria", blank=True)

    class Meta:
        verbose_name = "postagem"
        verbose_name_plural = "postagens"
        ordering = ["-data_adicao"]

    def save(self, *args, **kwargs):
        super().save() # salva a imagem primeiro

        img = Image.open(self.foto.path) # Abrindo imagem usando SELF

        if img.height > 400 or img.width > 800:
            nova_foto = (1200,800)
            img.thumbnail(nova_foto)
            img.save(self.foto.path) # Salva nova imagem no mesmo local

    def __str__(self):
        return self.titulo
    

class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

