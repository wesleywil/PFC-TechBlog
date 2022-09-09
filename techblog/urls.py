"""techblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403,handler404, handler500)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from contas.views import HomepageView, CriarContaView
from contas.forms import MeuLoginForm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),
    path('blog/', include('postagens.urls', namespace='blog')),
    path('perfil/', include('contas.urls', namespace='perfil')),
    path('login/', LoginView.as_view(authentication_form=MeuLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', CriarContaView.as_view(), name='registro'),
]

handler404 = "contas.views.pagina_nao_encontrada_view"
handler400 = "contas.views.pagina_requisicao_negadada"
handler403 = "contas.views.pagina_permissao_negada_view"
handler500 = "contas.views.pagina_error_view"
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)