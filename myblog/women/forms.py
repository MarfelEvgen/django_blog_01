from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import Form
from django.shortcuts import redirect

from .models import *


class AddPost1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "No Category"

    class Meta:
        model = Women
        field = ('title', 'slug', 'content', 'photo', 'is_published', 'cat')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-label mb-10',
                'placeholder': 'Enter Title'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control form-label mb-10'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control form-label textarea',
                'placeholder': 'Enter Text'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input mb-3 ',
                'type': 'checkbox'
            }),
            'cat': forms.Select(attrs={
                'class': 'form-select mb-3'
            })
            }
        exclude = ()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("There is something wrong with this field")

        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 100:
            raise ValidationError("The text should be longer")

        return content


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Username'
    }))
    password1 = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Password'
    }))
    password2 = forms.CharField(label=("Password confirmation"), widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Password Again'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Password'
    }))

    class Meta:
        model = User
        field = ('username', 'password')


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Tour Name'
    }))
    email = forms.CharField(label=("Email"), widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter Email'
    }))
    content = forms.CharField(label=("Message"), widget=forms.Textarea(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your Message'
    }))

    class Meta:
        fields = ('name', 'email', 'content',)

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')