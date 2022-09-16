from django.shortcuts import render, reverse, redirect
from django.views import generic
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail

from .models import Usuario

from .forms import CriarUsuarioCustomizadoForm, EditarUsuarioSimplesForm, TrocadeSenhaForm

from postagens.models import Postagem

User = get_user_model()



class HomepageView(generic.TemplateView):
    template_name = "homepage.html"

class AjudaView(generic.TemplateView):
    template_name = "ajuda.html"

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
            form = EditarUsuarioSimplesForm(request.POST, request.FILES, instance = usuario)
            if form.is_valid():
                form.save()
                return redirect("/perfil/")
        else:
            context["usuario"] = usuario
            context["form"] = form 
            return render(request, "editar_perfil.html", context)
    else:
        return redirect("/login/")

class AtualizarSenhaContaView(LoginRequiredMixin, generic.FormView):
    template_name = "mudar_senha.html"
    form_class = TrocadeSenhaForm
    model = User

    def get_form_kwargs(self):
        kwargs = super(AtualizarSenhaContaView, self).get_form_kwargs()
        kwargs['user'] = self.request.user 
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs 

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(AtualizarSenhaContaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('meu_perfil')


    

class MeuPerfilView(LoginRequiredMixin, generic.TemplateView):
    template_name = "meu_perfil.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(autor__usuario__id = self.request.user.id)
        data['ultimo_post'] = postagens.first()
        data['contagem_posts'] = postagens.count()
        return data

class MeusPostsView(LoginRequiredMixin, generic.ListView):
    template_name = "postagens/listar_postagens.html"
    context_object_name = "postagens"
    model = Postagem

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        postagens = Postagem.objects.filter(autor__usuario__id = self.request.user.id)
        data['postagens'] = postagens
        data['mensagem'] = f"do {self.request.user.username}"
        return data


def pagina_nao_encontrada_view(request, exception):
    return render(request, 'errors/404.html', exception)

def pagina_error_view(request, exception=None):
    return render(request, "errors/500.html",{})

def pagina_permissao_negada_view(request, exception=None):
    return render(request, "errors/403.html", {})

def pagina_error_csrf_view(request, reason=""):
    ctx = {'message': 'Voce não tem permissão para realizar está ação'}
    return render(request, 'errors/403_csrf.html', ctx)

def pagina_requisicao_negadada(request, exception=None):
    return render(request, "errors/400.html",{})