import status as status
from django.db import models

from apps.usuario.models import Usuario
from utils.core import STATUS


class Solicitacao(models.Model):
    cliente = models.ForeignKey(Usuario, models.DO_NOTHING, related_name='solicitacoes_cliente')
    lavanderia = models.ForeignKey(Usuario, models.DO_NOTHING, related_name='solicitacoes_lavanderia', null=True,
                                   blank=True)
    qtd = models.IntegerField('qtd de peças')
    status = models.CharField('status', max_length=20, choices=STATUS, default='ABERTO')

    class Meta:
        verbose_name = 'solicitação'
        verbose_name_plural = 'solicitações'

    def __str__(self):
        return 'qtd de peças %d, status %s' % (self.qtd, self.status)
