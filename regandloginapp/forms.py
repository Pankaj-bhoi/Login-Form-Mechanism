from django import forms
from .models import Reg
from django import forms

class RegForm(forms.Form):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter first name'
            }
        )
    )

    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter last name'
            }
        )
    )

    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter user name'
            }
        )
    )

    pwd = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter password'
            }
        )
    )

    mobile = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter number'
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter email address'
            }
        )
    )

    dob = forms.CharField(
        widget=forms.DateInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter Date of birth'
            }
        )
    )

    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'enter lasr name'
            }
        )
    )

class LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput)