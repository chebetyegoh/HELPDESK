from dataclasses import fields
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from base.models import Users


class RegisterFormStudent(UserCreationForm):
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Your Email'}),
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Last Name',
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Last Name'}),
    )

    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Username'}),
    )

    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Password', 'minlength': 8}),
    )

    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Password Again', 'minlength': 8}),
    )

    # reg_no = forms.CharField(
    #     max_length=100,
    #     required=True,
    #     help_text='Enter Reg no.',
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-group','placeholder': 'Registration Number'}),)

    class Meta:

        model = Users
        fields = [
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2',
        ]


class LoginStudentForm(AuthenticationForm):
    username = forms.CharField(
        max_length=200,
        required=True,
        help_text='Enter Username',
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Password', 'minlength': 8}),
    )

    class Meta:

        model = Users
        fields = ["username", "password"]

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     if not Users.objects.filter(username).exists():
    #         raise forms.ValidationError(
    #             "User with this username doesnot exist! Create an account instead")
    #     return username
