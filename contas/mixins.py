from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect,render

class AdminAndLoginRequired(AccessMixin):
    """ Verifica se o usuario esta logado e é um administrador """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.admin:
            context = {"message":"Voce não tem autorização para fazer está ação ou não está logado"}
            return render(request, "homepage.html", context)
        return super().dispatch(request, *args, **kwargs)

class AdminOrOwnerRequired(AccessMixin):
    """ Verifica se o usuario é um admininstrador ou se é o autor do post """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            if request.user.admin or self.get_object().autor_id == request.user.id:
                return super().dispatch(request, *args, **kwargs)
            else:
                context = {"message":"Ops! Está ação é apenas para administradores ou o autor do post"}
                return render(request, "homepage.html", context)
        else:
            context = {"message":"Está ação é apenas para usuarios logados!"}
            return render(request, "homepage.html", context)