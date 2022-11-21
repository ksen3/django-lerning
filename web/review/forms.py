from .models import review
from django.forms import ModelForm, TextInput, DateInput, Textarea, NumberInput

class reviewForm(ModelForm):
    class Meta:
        model = review
        fields = ['firstName', 'lastName', 'birth', 'grade', 'text']

        widgets = {
            'firstName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),

            'lastName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),

            'birth': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения',
            }),

            'grade': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оценка от 1 до 10',
                'max': '10',
                'min': '1',
            }),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш отзыв...',
            }),
        }