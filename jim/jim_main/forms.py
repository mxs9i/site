from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class CreateTreningForm(forms.ModelForm) : 
    

    class Meta:
        model = Trenings
        fields = ['trener', 'hall',
                  'dt']
        widgets = {
            'dt' : forms.DateTimeInput(attrs={'name':"filter-date", 'id':"filter-date", 'class' : 'input-field'})
        }

class LogInForm(AuthenticationForm):

    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя пользователя'}))

    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'input100', 'placeholder': 'Пароль'}))


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя'}))
    username = forms.CharField(label='username', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Имя пользователя'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Фамилия'}))
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label='repassword', widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Повтор пароля'}))
    email = forms.CharField(label='email', widget=forms.TextInput(
        attrs={'class': 'input100', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
