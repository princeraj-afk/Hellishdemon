from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_crispy_bulma.forms import EmailField


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()

    email = EmailField(
        label="email",
        required=True
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
