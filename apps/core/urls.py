from django.contrib import admin
from django.urls import path

from apps.core.views import HomeView, SolicitacaoCreate

urlpatterns = [
    path('', HomeView.as_view(), name=HomeView.name),
    path('solicitacao/criar/', SolicitacaoCreate.as_view(), name=SolicitacaoCreate.name)
]
