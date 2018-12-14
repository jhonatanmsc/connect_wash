from django.contrib import admin
from django.urls import path

from apps.core.views import HomeView, SolicitacaoCreate, SolicitacaoDelete

urlpatterns = [
    path('', HomeView.as_view(), name=HomeView.name),
    path('solicitacao/criar/', SolicitacaoCreate.as_view(), name=SolicitacaoCreate.name),
    path('solicitacao/<int:pk>/delete/', SolicitacaoDelete.as_view(), name=SolicitacaoDelete.name),
]
