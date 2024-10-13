from .models import Title, Tasks
from django.forms import ModelForm, TextInput, TimeInput, Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            })
        }


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = [
            'description',
            # 'category',
            'time'
        ]

        widgets = {
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача'
            }),
            # 'category': Select(attrs={
            #     'class': 'form-select',
            #     'placeholder': 'Блок'
            # }),
            'time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время'
            })
        }


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }),

    )

    class Meta:
        model = User
        fields = ('username', 'password')