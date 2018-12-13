from django import forms

from apps.core.models import Solicitacao
from utils.core import STATUS


class SolicitacaoForm(forms.ModelForm):
    # cliente = forms.CharField(label='cliente', required=False, max_length=30, widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    # lavanderia = forms.CharField(label='lavanderia', required=False, max_length=30, widget=forms.TextInput(attrs={
    #     'class': 'form-control'
    # }))
    qtd = forms.IntegerField(label='Quantidade', min_value=1, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    # status = forms.ChoiceField(label='Status', choices=STATUS, required=False, widget=forms.Select(attrs={
    #     'class': 'form-control'
    # }))
    # valor = forms.DecimalField(label='Valor', max_digits=9, required=False, decimal_places=2)

    class Meta:
        model = Solicitacao
        fields = '__all__'
