from django.contrib import admin
from django.urls import path

from apps.usuario.views import UsuarioCreate, UsuarioUpdate

urlpatterns = [
    path('usuario/criar/', UsuarioCreate.as_view(), name=UsuarioCreate.name),
    path('usuario/meus-dados/', UsuarioUpdate.as_view(), name=UsuarioUpdate.name)
]
