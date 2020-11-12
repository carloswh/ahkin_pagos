# Django
from django import forms

# Models
from ahkin_pagos.apps.custom_user.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
