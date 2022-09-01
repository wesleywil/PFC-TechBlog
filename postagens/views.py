import http
from django.shortcuts import render, redirect, reverse,HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import generic

from .models import Postagem, Categoria
from .forms import PostagemModelForm, CategoriaModelForm

from contas.models import Perfil
from contas.mixins import AdminAndLoginRequired

class ListarPosts(generic.ListView):
    template_name = "postagens/listar_postagens.html"
    context_object_name = "postagens"
    model = Postagem

class VerDetalhesPosts(generic.DetailView):
    template_name = "postagens/detalhes_postagem.html"
    context_object_name= "postagem"
    model = Postagem

class CriarPost(LoginRequiredMixin, generic.CreateView):
    template_name = "postagens/form_postagem.html"
    form_class = PostagemModelForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['acao'] = "Criar nova postagem"
        data['botao'] = "Criar"
        return data
    
    def form_valid(self, form):
        perfil = Perfil.objects.get(pk = self.request.user.pk)
        obj = form.save(commit=False)
        obj.dono = perfil
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("blog:listar_posts")
    

class AtualizarPost(UserPassesTestMixin, generic.UpdateView):
    template_name = "postagens/form_postagem.html"
    context_object_name = "postagem"
    form_class = PostagemModelForm
    model = Postagem
    queryset = Postagem.objects.all()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['acao'] = "Atualizar Postagem"
        data['botao'] = "Atualizar"
        return data

    def test_func(self):
        return self.get_object().dono_id == self.request.user.pk

class ListarCategorias(generic.ListView):
    template_name = "categorias/listar_categorias.html"
    context_object_name = "categorias"
    model = Categoria

class VerDetalhesCategorias(generic.DetailView):
    template_name = "categorias/detalhes_categoria.html"
    context_object_name = "categoria"
    model = Categoria

class CriarCategoria(AdminAndLoginRequired, generic.CreateView):
    template_name = "categorias/form_categoria.html"
    form_class = CategoriaModelForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['acao'] = "Criar nova categoria"
        data['botao'] = "Criar"
        return data

class AtualizarCategoria(AdminAndLoginRequired, generic.UpdateView):
    template_name = "categorias/form_categoria.html"
    context_object_name = "categoria"
    form_class = CategoriaModelForm
    model = Categoria
    queryset = Categoria.objects.all()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['acao'] = "Atualizar categoria"
        data['botao'] = "Atualizar"
        return data


