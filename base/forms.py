from django import forms



class Signup(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='First Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
