# Django
from django import forms
from django.contrib.auth.models import Group
from django.template.defaultfilters import slugify

from ahkin_pagos.apps.empresa.models import Empresa
from ahkin_pagos.apps.custom_user.models import User


class NewSignUpForm(forms.ModelForm):
    nombre_empresa = forms.CharField(max_length=30, label='Nombre empresa', widget=forms.TextInput(
        attrs={'placeholder': 'Nombre Empresa', 'class': 'form-control', 'data-rule-required': "true"}))
    password = forms.CharField(label='Password Portal Cliente')

    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'email', 'password']

    def clean(self):
        cleaned_data = super(NewSignUpForm, self).clean()
        empresa = cleaned_data['nombre_empresa']
        try:
            Empresa.objects.get(nombre=cleaned_data['nombre_empresa'])
            raise forms.ValidationError('Ya existe una empresa con este nombre')
        except Empresa.DoesNotExist:
            pass

        return cleaned_data

    def save(self, commit=True):
        # Se crea empresa
        nueva_empresa = super(NewSignUpForm, self).save(commit=False)
        nueva_empresa.nombre = self.cleaned_data['nombre_empresa']
        nueva_empresa.slug = slugify(self.cleaned_data['nombre_empresa'])

        # Se valida si ya existe el slug
        slug_temporal = nueva_empresa.slug
        existe_slug = True
        contador = 0
        while existe_slug and contador < 100:
            if Empresa.objects.filter(slug=nueva_empresa.slug).exists():
                contador = contador + 1
                nueva_empresa.slug = slug_temporal + str(contador)
            else:
                existe_slug = False

        nueva_empresa.email = self.cleaned_data['email']
        nueva_empresa.save()

        user = User.objects.create_user(
            username="admin@%s" % nueva_empresa.slug,
            email=self.cleaned_data['email'],
            # company=company,
        )
        user.set_password(self.cleaned_data['password'])

        g, created = Group.objects.get_or_create(name="Administrador")
        user.groups.add(g)
        user.save()

        def __init__(self, *args, **kwargs):
            super(NewSignUpForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget = forms.TextInput(attrs={'placeholder': "E-mail", 'type': 'email',
                                                                 'class': 'form-control', 'data-rule-required': "true",
                                                                 "data-rule-email": 'true'})
            self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': "Password",
                                                                        'class': 'form-control',
                                                                        'data-rule-required': "true"})
