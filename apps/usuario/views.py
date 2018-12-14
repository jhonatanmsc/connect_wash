from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from apps.localidade.models import Cidade, Bairro
from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario


class UsuarioList(TemplateView):
    name = 'usuario-list'
    template_name = 'usuario-list.html'
    model = Usuario


class UsuarioCreate(CreateView):
    name = 'usuario-create'
    template_name = 'usuario/usuario-create.html'
    model = Usuario
    success_message = 'Usuario %s criado.'
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super(UsuarioCreate, self).get_context_data(**kwargs)
        context['cidades'] = Cidade.objects.all()
        context['bairros'] = Bairro.objects.all()
        return context

    def form_valid(self, form):
        z_usuario = form.save(commit=False)
        z_nome = form.cleaned_data['nome']
        z_email = form.cleaned_data['email']
        z_perfil = form.cleaned_data['perfil']
        z_logradouro = form.cleaned_data['logradouro']
        z_cidade = form.cleaned_data['cidade']
        z_bairro = form.cleaned_data['bairro']
        z_cep = form.cleaned_data['cep']

