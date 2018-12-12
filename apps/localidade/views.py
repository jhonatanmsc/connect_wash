from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from apps.localidade.models import Cidade


class CidadeList(TemplateView):
    name = 'cidade-list'
    template_name = 'cidade-list.html'
    model = Cidade


class CidadeCreate(CreateView):
    name = 'cidade-create'
    template_name = 'cidade-create.html'
    model = Cidade
    # form = CidadeForm
