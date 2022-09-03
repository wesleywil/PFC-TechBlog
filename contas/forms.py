from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm

User = get_user_model()


class MeuLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        field_classes = {'username':UsernameField}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'w-full border-2 bg-white/40  text-xl m-2 rounded-xl pl-1'})
        self.fields['password'].widget.attrs.update({'class':'w-full border-2 bg-white/40  text-xl m-2 rounded-xl pl-1'})

class CriarUsuarioCustomizadoForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'foto',
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            
        )
        field_classes = {'username':UsernameField}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['email'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['first_name'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['last_name'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['foto'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['password1'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1 '})
        self.fields['password2'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})