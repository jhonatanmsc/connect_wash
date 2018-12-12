from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from apps.usuario.models import Usuario


class UsuarioList(TemplateView):
    name = 'usuario-list'
    template_name = 'usuario-list.html'
    model = Usuario


class UsuarioCreate(CreateView):
    name = 'usuario-create'
    template_name = 'usuario-create.html'
    model = Usuario
    # form = CidadeForm
