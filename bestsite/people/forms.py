from django.core.exceptions import ValidationError

from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, Select, CheckboxInput

class PeopleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

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
                'class': 'form-check',
                'placeholder': 'Input content'
            })
        }

    # Создаем собственный валидатор на проверку длины поля title
    # Функия должна начинаться с префикса clean_[имя поля которое хотим проверить]
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise ValidationError('Длина превышает 10 символов')
        return title

# ----------------------------------------------------------------