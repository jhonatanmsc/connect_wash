import pdb
from decimal import Decimal

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from apps.core.forms import SolicitacaoForm
from apps.core.models import Solicitacao
from apps.usuario.models import Usuario
from utils.core import STATUS


class HomeView(TemplateView):
    name = 'home'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['solicitacoes'] = Solicitacao.objects.all().order_by('status')
        return context


class SolicitacaoList(ListView):
    name = 'solicitacao-list'
    template_name = 'core/solicitacao-list.html'
    model = Solicitacao

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SolicitacaoList, self).get_context_data(**kwargs)
        context['solicitacoes'] = Solicitacao.objects.filter(lavanderia=self.request.user)
        return context


class SolicitacaoCreate(SuccessMessageMixin, CreateView):
    name = 'solicitacao-create'
    template_name = 'core/solicitacao-create.html'
    model = Solicitacao
    form_class = SolicitacaoForm
    success_message = 'Solicitacao criada.'

    def get_context_data(self, **kwargs):
        context = super(SolicitacaoCreate, self).get_context_data(**kwargs)
        context['lavanderias'] = Usuario.objects.filter(perfil='LAVANDERIA')
        context['status'] = [stts[0] for stts in STATUS]
        return context

    def form_valid(self, form):
        try:
            # z_solicitacao = form.save(commit=False)
            z_cliente = self.request.user
            z_lavanderia = form.cleaned_data['lavanderia']
            z_qtd = int(form.cleaned_data['qtd'])
            z_status = 'ABERTO'
            z_solicitacao = Solicitacao(cliente=z_cliente, lavanderia=z_lavanderia, qtd=z_qtd, status=z_status)
            z_solicitacao.save()
            messages.success(self.request, self.success_message)
            return redirect('home')

        except Exception as e:
            messages.error(self.request, e)
            return redirect(self.name)

    def form_invalid(self, form):
        for erro in form.errors:
            messages.add_message(self.request, messages.ERROR, erro)
        return redirect(self.name)


class SolicitacaoDelete(SuccessMessageMixin, DeleteView):
    name = 'solicitacao-delete'
    model = Solicitacao
    success_message = 'Solicitação deletada'
    success_url = reverse_lazy('home')

    def get_success_message(self, cleaned_data):
        messages.success(self.request, self.success_message)
        return self.success_url


class SolicitacaoUpdate(SuccessMessageMixin, UpdateView):
    name = 'solicitacao-update'
    template_name = 'core/solicitacao-create.html'
    model = Solicitacao
    success_message = 'Solicitação alterada.'
    form_class = SolicitacaoForm

    def get_context_data(self, **kwargs):
        context = super(SolicitacaoUpdate, self).get_context_data(**kwargs)
        context['lavanderias'] = Usuario.objects.filter(perfil='LAVANDERIA')
        context['status'] = [stts[0] for stts in STATUS]
        return context

    def form_valid(self, form):
        try:
            z_solicitacao = form.save(commit=False)
            if self.request.user.perfil == 'CLIENTE':
                z_cliente = self.request.user
                z_lavanderia = form.cleaned_data['lavanderia']
                z_qtd = int(form.cleaned_data['qtd'])
                z_status = 'ABERTO'
                z_solicitacao.cliente = z_cliente
                z_solicitacao.lavanderia = z_lavanderia
                z_solicitacao.qtd = z_qtd
                z_solicitacao.status = z_status
                z_solicitacao.save()
                messages.success(self.request, self.success_message)
                return redirect('home')
            else:
                z_solicitacao = Solicitacao.objects.get(id=z_solicitacao.id)
                z_lavanderia = self.request.user
                z_valor = form.cleaned_data['valor']
                z_status = 'PENDENTE'
                z_solicitacao.lavanderia = z_lavanderia
                z_solicitacao.valor = z_valor
                z_solicitacao.status = z_status
                z_solicitacao.save()
                return redirect('home')

        except Exception as e:
            messages.error(self.request, e)
            return redirect(self.name)

    def form_invalid(self, form):
        # pdb.set_trace()
        for erro in form.errors:
            messages.add_message(self.request, messages.ERROR, erro)
        return redirect(self.name)


class SolicitacaoCancel(SuccessMessageMixin, TemplateView):
    name = 'solicitacao-cancel'
    success_message = 'Solicitacao cancelada'

    def post(self, request, pk):
        z_solicitacao = Solicitacao.objects.get(id=pk)
        z_solicitacao.lavanderia = None
        z_solicitacao.status = 'ABERTO'
        z_solicitacao.valor = '0,00'
        z_solicitacao.save()
        messages.success(request, self.success_message)
        return redirect('solicitacao-list')


class SolicitacaoAccept(SuccessMessageMixin, TemplateView):
    name = 'solicitacao-accept'
    success_message = 'Solicitacao aceita'

    def post(self, request, pk):
        z_solicitacao = Solicitacao.objects.get(id=pk)
        z_solicitacao.status = 'ATENDIDO'
        z_solicitacao.save()
        messages.success(request, self.success_message)
        return redirect('home')


class SolicitacaoDenied(SuccessMessageMixin, TemplateView):
    name = 'solicitacao-denied'
    success_message = 'Solicitação negada'

    def post(self, request, pk):
        z_solicitacao = Solicitacao.objects.get(id=pk)
        z_solicitacao.lavanderia = None
        z_solicitacao.status = 'ABERTO'
        z_solicitacao.valor = '0,00'
        z_solicitacao.save()
        messages.success(request, self.success_message)
        return redirect('home')

