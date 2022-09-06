from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _



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

class EditarUsuarioSimplesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'foto',
            'username',
            'email',
            'first_name',
            'last_name'
        )
        field_classes = {'username':UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['email'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['first_name'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['last_name'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})
        self.fields['foto'].widget.attrs.update({'class':'w-full border-2 bg-white/40  m-2 rounded-xl pl-1'})


class MeuSetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch': _('Senhas não combinam.'),
    }
    new_password1 = forms.CharField(
        label=_("Nova Senha"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'w-full text-black'}),
        strip=False,
        
    )
    new_password2 = forms.CharField(
        label=_("Confirmação de Nova Senha"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'w-full text-black'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class TrocadeSenhaForm(MeuSetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = {
        **MeuSetPasswordForm.error_messages,
        'password_incorrect': _("Sua senha antiga foi não confere, Por favor tente novamente."),
    }
    old_password = forms.CharField(
        label=_("Senha Antiga"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True , 'class':'w-full text-black'}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password