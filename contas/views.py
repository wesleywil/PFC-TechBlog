from django.shortcuts import render, reverse
from django.views import generic

from .forms import CriarUsuarioCustomizadoForm

from postagens.models import Postagem

class HomepageView(generic.TemplateView):
    template_name = "homepage.html"

class CriarConta(generic.CreateView):
    template_name = "registration/registro.html"
    form_class = CriarUsuarioCustomizadoForm

    def get_success_url(self):
        return reverse('login')

class MeuPerfilView(generic.TemplateView):
    template_name = "meu_perfil.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(dono__usuario__id = self.request.user.id)
        data['ultimo_post'] = postagens.first()
        data['contagem_posts'] = postagens.count()
        return data

class MeusPostsView(generic.ListView):
    template_name = "postagens/listar_postagens.html"
    context_object_name = "postagens"
    model = Postagem

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(dono__usuario__id = self.request.user.id)
        data['postagens'] = postagens
        data['mensagem'] = f"do {self.request.user.username}"
        return data
