from django.shortcuts import render, reverse
from django.views import generic
from django.core.mail import send_mail

from .forms import CriarUsuarioCustomizadoForm

from postagens.models import Postagem

class HomepageView(generic.TemplateView):
    template_name = "homepage.html"

class CriarConta(generic.CreateView):
    template_name = "registration/registro.html"
    form_class = CriarUsuarioCustomizadoForm

    def get_success_url(self):
        return reverse('login')
    
    def form_valid(self,form):
        usuario = form.save(commit = False)
        usuario.save()
        send_mail(
            subject="Conta no TechBlog Criada com Sucesso",
            message="Bem vindo, agora você faz parte do maior blog de tecnologia do mundo",
            from_email="admin@techblog_test.com",
            recipient_list=[usuario.email]
        )
        return super(CriarConta, self).form_valid(form)

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
