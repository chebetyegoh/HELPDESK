from dataclasses import fields
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm,UserChangeForm
from django.forms import ModelForm
from base.models import Users, Student, StudentProfile,Ticket
from django.db import transaction
from django.core.exceptions import ValidationError


class SignupStudent(UserCreationForm):
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

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']
        return first_name

    def clean_lastname(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = Users.objects.filter(username=username)
        if new.count():
            raise ValidationError("User with username already Exist!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = Users.objects.filter(email=email)
        if new.count():
            raise ValidationError(" Email Already Exist")
        return email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Passwords don't match")
    #     return password2

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = Users.objects.create_user(
            self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user

    class Meta():

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
    #      username = self.cleaned_data.get("username").lower()
    #      if not Users.objects.filter(username).exists():
    #          raise forms.ValidationError(
    #              "User with this username doesnot exist! Create an account instead")
    #      return username


class MyChangeFormPassword(PasswordChangeForm):
    old_password = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Current Password', 'minlength': 8}),
    )

    new_password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': ' New Password', 'minlength': 8}),
    )

    new_password2 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Confirm Password', 'minlength': 8}),
    )

    class Meta:

        model = Users
        fields = ["old_password", "new_password1", "new_password2"]


class EditProfile(UserChangeForm):

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


    class Meta():

        model = Users
        fields = [
            'username', 'email', 'first_name', 'last_name']
        exclude = ('password',)



        

class RaiseTicketForm(forms.ModelForm):
    ticket_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Name',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Name'}),
    )

    ticket_type = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Type',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Type'}),
    )

    ticket_description = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Description',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Description'}),
    )

    class Meta():

        model = Ticket
        fields = [
            'ticket_name', 'ticket_type', 'ticket_description',
        ]
        exclude = ('created_by',)

class EditTicketForm(forms.ModelForm):

    ticket_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Name',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Name'}),
    )

    ticket_type = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Type',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Type'}),
    )

    ticket_description = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Ticket Description',
        widget=forms.TextInput(
            attrs={'class': 'input--style-5', 'placeholder': 'Ticket Description'}),
    )

    class Meta():

        model = Ticket
        fields = [
            'ticket_name', 'ticket_type', 'ticket_description',
        ]
        exclude = ('created_by',)


class LoginOfficerForm(AuthenticationForm):
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