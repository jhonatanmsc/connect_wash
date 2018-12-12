from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from apps.core.models import Solicitacao


class HomeView(TemplateView):
    name = 'home'
    template_name = 'index.html'


class SolicitacaoList(ListView):
    name = 'solicitacao-list'
    template_name = 'solicitacao-list.html'
    model = Solicitacao


class SolicitacaoCreate(CreateView):
    name = 'solicitacao-create'
    template_name = 'solicitacao-create.html'
    model = Solicitacao
    # form = SolicitacaoForm
