# Create your models here.

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission
from apps.localidade.models import Endereco
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('Usuarios devem ter cpfs validos!')

        user = self.model(
            cpf_cnpj=self.normalize_email(email),
            nome=nome,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(
            email,
            password=password,
            nome=nome,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Perfil(models.Model):
    tipo = models.CharField('cargo', max_length=100)
    permissoes = models.ManyToManyField(
        Permission,
        verbose_name='Permissões',
        blank=True,
    )

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return self.cargo


class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf_cnpj = models.CharField(u'cpf/cnpj', max_length=19, unique=True)
    nome = models.CharField(u'nome', max_length=100)
    email = models.EmailField(u'email', max_length=255, null=True, unique=True)
    telefone = models.CharField('numero de telefone', max_length=30, null=True, blank=True)
    data_nasc = models.DateField(null=True, blank=True)
    adress = models.ForeignKey(Endereco, models.DO_NOTHING, null=True, blank=True)
    perfil = models.ForeignKey(u'Perfil', models.DO_NOTHING,related_name='usuario', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super(Usuario, self).save()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def first_name(self):
        return self.nome.split(' ')[0]
