from django.urls import path

from .views import MeuPerfilView, EditarContaView, AtualizarSenhaContaView, MeusPostsView


app_name = "perfil"

urlpatterns = [
    path('',MeuPerfilView.as_view(), name='meu_perfil'),
    path('editar/', EditarContaView, name='editar_perfil'),
    path('editar_senha/', AtualizarSenhaContaView.as_view(), name="editar_senha"),
    path('posts/', MeusPostsView.as_view(), name='minhas_postagens'),
]