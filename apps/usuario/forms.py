from django import forms

from apps.usuario.models import Usuario
from utils.usuarios import perfils


class UsuarioForm(forms.ModelForm):
    cpf_cnpj = forms.CharField(label='cpf/cnpj', max_length=19, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    nome = forms.CharField(label='nome', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='email', max_length=100, required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    telefone = forms.CharField(label='numero de telefone', required=False, max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    data_nasc = forms.DateField(label='data do nascimento', required=False, widget=forms.DateInput(attrs={
        'class': 'form-control'
    }))
    perfil = forms.ChoiceField(label='perfil', max_length=20, choices=perfils, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    logradouro = forms.CharField(label='logradouro', max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    numero = forms.IntegerField(label='numero', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Usuario
        fields = '__all__'
