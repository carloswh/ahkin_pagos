# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# ==== Django ====
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

# === Import ===
import uuid

# Create your models here.

phone_regex = RegexValidator(regex=r'^\d{8,14}((,\d{8,14})?)*$',
                             message="El formato del teléfono debe ser: '9998888777', "
                                     "sin código de país. De 8-14 dígitos permitidos. "
                                     "Puede agregar más telefonos seperados por coma.")


class User(AbstractUser):
    ADMIN = 'Admin'
    TECNICO = 'Tec'
    VENTAS = 'Ventas'
    TYPE = (
        (ADMIN, 'Administrador'),
        (TECNICO, 'Técnico'),
        (VENTAS, 'Ventas')
    )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator, MinLengthValidator(5)],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    direccion = models.TextField(blank=True, verbose_name="Dirección")
    telefono = models.CharField(validators=[phone_regex], max_length=250, blank=True, verbose_name="Telefono Celular")
    tipo = models.CharField(choices=TYPE, default=ADMIN, blank=False, verbose_name="Tipo de Usuario", max_length=15)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return '{}'.format(self.username)
