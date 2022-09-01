from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect,render

class AdminAndLoginRequired(AccessMixin):
    """ Verifica se o usuario esta logado e é um administrador """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.admin:
            context = {"message":"Voce não tem autorização para fazer está ação ou não está logado"}
            return render(request, "homepage.html", context)
        return super().dispatch(request, *args, **kwargs)