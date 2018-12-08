from django.db import models

from django.db import models
from utils.localidade import *


class Endereco(models.Model):
    cep = models.CharField(verbose_name='CEP', max_length=9)
    cidade = models.ForeignKey('Cidade', models.DO_NOTHING, null=True)
    bairro = models.ForeignKey('Bairro', models.DO_NOTHING, null=True)
    logradouro = models.CharField(verbose_name='Logradouro', max_length=100, null=True)
    numero = models.CharField(verbose_name='Número', max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    referencia = models.CharField(verbose_name='Referência', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return '%s, %s' % (self.bairro.nome, self.cidade)


class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    uf = models.CharField(max_length=2, choices=UFs, verbose_name="UF")

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']

    def __str__(self):
        return '%s %s' % (self.nome, self.uf)


class Bairro(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cidade = models.ForeignKey('Cidade', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        ordering = ['nome']

    def __str__(self):
        return '%s %s' % (self.nome, self.cidade)
