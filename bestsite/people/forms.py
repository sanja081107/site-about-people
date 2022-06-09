from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, Select, CheckboxInput

class PeopleForm(ModelForm):
    captcha = CaptchaField(label='Введите текст с картинки ')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
        self.fields['content'].label = 'Контент'

    class Meta:
        model = People
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input slug'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input content',
                'rows': '5',
                'cols': '45'
            }),
            'photo': FileInput(attrs={
                'type': 'file',
                'accept': 'image/*'
            }),
            'cat': Select(attrs={
                'class': 'form-control',
            }),
            'is_published': CheckboxInput(attrs={
                'class': 'form-check'
            })
        }

    # Создаем собственный валидатор на проверку длины поля title
    # Функия должна начинаться с префикса clean_[имя поля которое хотим проверить]
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 10 символов')
        return title

# ----------------------------------------------------------------

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input login'}))
    slug = forms.SlugField(label='Url', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input URL'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input password'}))
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input password again'}))
    email = forms.CharField(label='Email (not required)', required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input email'}))
    photo = forms.ImageField(label='Your photo (not required)', required=False, widget=forms.FileInput(attrs={'type': 'file', 'accept': 'image/*'}))
    birthday = forms.DateTimeField(label='Birthday (not required)', required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    context = forms.CharField(label='About(not required)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About you', 'rows': '7'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'slug', 'photo', 'email', 'birthday', 'context', 'password1', 'password2')
        # widgets = {'slug': forms.HiddenInput()}

class UpdateUserForm(ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input login'}))
    slug = forms.SlugField(label='Url', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input URL'}))
    email = forms.CharField(label='Email (not required)', required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input email'}))
    photo = forms.ImageField(label='Your photo (not required)', required=False, widget=forms.FileInput(attrs={'type': 'file', 'accept': 'image/*'}))
    birthday = forms.DateTimeField(label='Birthday (not required)', required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
    context = forms.CharField(label='About(not required)', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'info', 'rows': '7'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'slug', 'photo', 'email', 'birthday', 'context')

# ----------------------------------------------------------------

class ChangeUserForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('slug', 'photo', 'birthday', 'context')

# ----------------------------------------------------------------

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input login'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input password'}))

    class Meta:
        model = CustomUser

# ----------------------------------------------------------------

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['context']
        widgets = {
            'context': Textarea(attrs={'class': 'form-control', 'placeholder': 'Input text', 'rows': '5'})
        }

# ----------------------------------------------------------------
