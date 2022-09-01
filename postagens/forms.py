from django import forms

from .models import Postagem, Categoria

class PostagemModelForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = (
            'titulo',
            'texto',
            'categorias',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class':'w-full border-2 bg-white/40 border-red-700 text-xl m-2 rounded-xl pl-1'})
        self.fields['texto'].widget.attrs.update({'class':'w-full border-2 bg-white/40 border-red-700 text-xl m-2 rounded-xl pl-1'})
        self.fields['categorias'].widget.attrs.update({'class':'w-full border-2 bg-white/40 border-red-700 text-xl m-2 rounded-xl pl-1'})

class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = (
            'titulo',
            'descricao',
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class':'w-full border-2 bg-white/40 border-red-700 text-xl m-2 rounded-xl pl-1'})
        self.fields['descricao'].widget.attrs.update({'class':'w-full border-2 bg-white/40 border-red-700 text-xl m-2 rounded-xl pl-1'})