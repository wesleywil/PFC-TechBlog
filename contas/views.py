from django.shortcuts import render, reverse
from django.views import generic

from .forms import CriarUsuarioCustomizadoForm

class HomepageView(generic.TemplateView):
    template_name = "homepage.html"

class CriarConta(generic.CreateView):
    template_name = "registration/registro.html"
    form_class = CriarUsuarioCustomizadoForm

    def get_success_url(self):
        return reverse('login')
