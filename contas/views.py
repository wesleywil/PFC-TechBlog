from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .models import Usuario

from .forms import CriarUsuarioCustomizadoForm, EditarUsuarioSimplesForm

from postagens.models import Postagem

class HomepageView(generic.TemplateView):
    template_name = "homepage.html"

class CriarContaView(generic.CreateView):
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
        return super(CriarContaView, self).form_valid(form)

def EditarContaView(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(pk = request.user.pk)
        form = EditarUsuarioSimplesForm(instance = usuario)
        context ={}
        if request.method == "POST":
            form = EditarUsuarioSimplesForm(request.POST, instance = usuario)
            if form.is_valid():
                form.save()
                return redirect("/perfil/")
        else:
            context["usuario"] = usuario
            context["form"] = form 
            return render(request, "editar_perfil.html", context)

    

class MeuPerfilView(LoginRequiredMixin, generic.TemplateView):
    template_name = "meu_perfil.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(dono__usuario__id = self.request.user.id)
        data['ultimo_post'] = postagens.first()
        data['contagem_posts'] = postagens.count()
        return data

class MeusPostsView(LoginRequiredMixin, generic.ListView):
    template_name = "postagens/listar_postagens.html"
    context_object_name = "postagens"
    model = Postagem

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(dono__usuario__id = self.request.user.id)
        data['postagens'] = postagens
        data['mensagem'] = f"do {self.request.user.username}"
        return data
