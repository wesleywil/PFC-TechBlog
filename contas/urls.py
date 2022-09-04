from django.urls import path

from .views import MeuPerfilView, MeusPostsView


app_name = "perfil"

urlpatterns = [
    path('',MeuPerfilView.as_view(), name='meu_perfil'),
    path('posts/', MeusPostsView.as_view(), name='minhas_postagens'),
]