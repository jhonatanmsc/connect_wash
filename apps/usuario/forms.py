from django import forms

from apps.usuario.models import Usuario
from utils.usuarios import perfils


class UsuarioForm(forms.ModelForm):
    cpf_cnpj = forms.CharField(label='cpf/cnpj', max_length=19, required=False, widget=forms.TextInput(attrs={
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
    perfil = forms.ChoiceField(label='perfil', choices=perfils, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    logradouro = forms.CharField(label='logradouro', max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    numero = forms.IntegerField(label='numero', required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    cidade = forms.CharField(label='Cidade', required=True, widget=forms.TextInput())
    bairro = forms.CharField(label='Bairro', required=True, widget=forms.TextInput())

    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['password'].required = False
            self.fields['perfil'].required = False

    def clean_password(self):
        if self.instance:
            return self.instance.password
        else:
            return self.cleaned_data['password']
