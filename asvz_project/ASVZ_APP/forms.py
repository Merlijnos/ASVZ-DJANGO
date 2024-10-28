from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Gebruikersnaam',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'input-field'})
    )
    password = forms.CharField(
        label='Wachtwoord',
        widget=forms.PasswordInput(attrs={'class': 'input-field'})
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input-field'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field'})
    )
    password1 = forms.CharField(
        label='Wachtwoord',
        widget=forms.PasswordInput(attrs={'class': 'input-field'})
    )
    password2 = forms.CharField(
        label='Wachtwoord bevestigen',
        widget=forms.PasswordInput(attrs={'class': 'input-field'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
