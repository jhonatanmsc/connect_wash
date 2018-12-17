from django.contrib import admin
from django.urls import path

from apps.core.views import HomeView, SolicitacaoCreate, SolicitacaoDelete, SolicitacaoUpdate, SolicitacaoList, \
    SolicitacaoCancel, SolicitacaoAccept, SolicitacaoDenied

urlpatterns = [
    path('', HomeView.as_view(), name=HomeView.name),
    path('solicitacao/', SolicitacaoList.as_view(), name=SolicitacaoList.name),
    path('solicitacao/criar/', SolicitacaoCreate.as_view(), name=SolicitacaoCreate.name),
    path('solicitacao/<int:pk>/deletar/', SolicitacaoDelete.as_view(), name=SolicitacaoDelete.name),
    path('solicitacao/<int:pk>/editar/', SolicitacaoUpdate.as_view(), name=SolicitacaoUpdate.name),
    path('solicitacao/<int:pk>/cancelar/', SolicitacaoCancel.as_view(), name=SolicitacaoCancel.name),
    path('solicitacao/<int:pk>/aceitar/', SolicitacaoAccept.as_view(), name=SolicitacaoAccept.name),
    path('solicitacao/<int:pk>/negar/', SolicitacaoDenied.as_view(), name=SolicitacaoDenied.name),
]
