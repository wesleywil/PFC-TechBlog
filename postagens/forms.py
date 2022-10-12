from django import forms

from .models import Postagem, Categoria

class PostagemModelForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = (
            'foto',
            'titulo',
            'texto',
            'categorias',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs.update({'class':'w-full '})
        self.fields['titulo'].widget.attrs.update({'class':'w-full '})
        # self.fields['texto'].widget.attrs.update({'class':'text-red-600'})
        self.fields['categorias'].widget.attrs.update({'class':'w-full'})

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = (
            'titulo',
            'descricao',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class':'w-full border-2 bg-white/40  text-xl m-2 rounded-xl pl-1'})
        self.fields['descricao'].widget.attrs.update({'class':'w-full border-2 bg-white/40  text-xl m-2 rounded-xl pl-1'})