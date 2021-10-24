from .models import Client, Call, Deal, Reminder
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name',
                  'lpr',
                  'position',
                  'tel_number',
                  'email',
                  'adress',
                  'commentary',
                  'publish']
        widgets = {
            'client_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название клиента'
            }),
            'lpr': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО ЛПРа'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность ЛПРа'
            }),
            'tel_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тел. номер'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'EMAIL'
            }),
            'adress': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес производства'
            }),
            'commentary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарии'
            }),
            'publish': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),

        }


class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['client',
                  'commentary',
                  'publish']
        widgets = {
            'commentary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарии'
            }),
            'publish': forms.DateTimeInput(attrs={
                'autocomplete': 'off',
                'class': 'form-control',
            }),
        }


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['client',
                  'event_type',
                  'commentary',
                  'deadline',
                  ]
        widgets = {
            'commentary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарии'
            }),
            'deadline': forms.DateTimeInput(attrs={
                    'autocomplete': 'off',
                    'placeholder': 'Дата напоминания'
            }),
        }


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['client',
                  'commentary',
                  'publish',
                  ]
        widgets = {
            'commentary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарии'
            }),
            'publish': forms.DateTimeInput(attrs={
                'autocomplete': 'off',
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
