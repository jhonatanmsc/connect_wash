import pdb

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView

from apps.localidade.models import Cidade, Bairro, Endereco
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
        z_cidade = Cidade.objects.get(id=form.cleaned_data['cidade'])
        z_bairro = Bairro.objects.get(id=form.cleaned_data['bairro'])
        z_password = form.cleaned_data['password']
        z_usuario.nome = z_nome
        z_usuario.email = z_email
        z_usuario.perfil = z_perfil

        z_endereco = ''
        try:
            z_endereco = Endereco.objects.get(Q(logradouro=z_logradouro) |
                                              Q(cidade=z_cidade) |
                                              Q(bairro=z_bairro))
        except Exception as e:
            z_endereco = Endereco(
                cidade=z_cidade,
                bairro=z_bairro,
                logradouro=z_logradouro
            )
            z_endereco.save()

        z_usuario.endereco = z_endereco
        z_usuario.set_password(z_password)
        z_usuario.is_superuser = True
        z_usuario.is_admin = True
        z_usuario.is_active = True
        z_usuario.is_staff = True
        z_usuario.save()
        return redirect('login')

    def form_invalid(self, form):
        # pdb.set_trace()
        for erro in form.errors:
            messages.add_message(self.request, messages.ERROR, erro)
        return redirect(self.name)


class UsuarioUpdate(SuccessMessageMixin, UpdateView):
    name = 'meus-dados'
    template_name = 'usuario/meus-dados.html'
    model = Usuario
    success_message = 'Usuario alterado.'
    form_class = UsuarioForm

    def get_object(self):
        return Usuario.objects.get(id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UsuarioUpdate, self).get_context_data(**kwargs)
        context['cidades'] = Cidade.objects.all()
        context['bairros'] = Bairro.objects.all()
        return context

    def form_valid(self, form):
        z_usuario = self.get_object()
        # pdb.set_trace()
        z_usuario.nome = form.cleaned_data['nome']
        z_logradouro = form.cleaned_data['logradouro']
        z_cidade = Cidade.objects.get(id=form.cleaned_data['cidade'])
        z_bairro = Bairro.objects.get(id=form.cleaned_data['bairro'])

        try:
            z_endereco = Endereco.objects.get(Q(logradouro=z_logradouro) &
                                              Q(cidade=z_cidade) &
                                              Q(bairro=z_bairro))
        except Exception as e:
            z_endereco = Endereco(
                cidade=z_cidade,
                bairro=z_bairro,
                logradouro=z_logradouro
            )
            z_endereco.save()
            pdb.set_trace()

        z_usuario.endereco = z_endereco
        z_usuario.is_superuser = True
        z_usuario.is_admin = True
        z_usuario.is_active = True
        z_usuario.is_staff = True
        z_usuario.save()
        # pdb.set_trace()
        return redirect('home')

    def form_invalid(self, form):
        # pdb.set_trace()
        for erro in form.errors:
            messages.add_message(self.request, messages.ERROR, erro)
        return redirect(self.name)
