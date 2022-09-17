from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image

class Usuario(AbstractUser):
    admin = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="usuarios/", default="usuarios/predefinido/businessman.png")

    def save(self, *args, **kwargs):
        super().save() # salva a imagem primeiro

        img = Image.open(self.foto.path) # Abrindo imagem usando SELF

        if img.height > 500 or img.width > 500:
            nova_foto = (500,500)
            img.thumbnail(nova_foto)
            img.save(self.foto.path) # Salva nova imagem no mesmo local

