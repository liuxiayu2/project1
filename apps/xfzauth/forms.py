from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2)
    telephone = forms.CharField(max_length=6, min_length=2)
    password = forms.CharField(min_length=2, max_length=20)
