from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    admin = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="usuarios/", default="usuarios/predefinido/businessman.png")

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.username

def signal_apos_criacao_de_usuario(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        Perfil.objects.create(usuario = instance)

post_save.connect(signal_apos_criacao_de_usuario, sender=Usuario)