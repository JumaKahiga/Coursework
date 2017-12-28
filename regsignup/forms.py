from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  SignupPage


class RegForm(forms.ModelForm):

	class Meta:
		model= SignupPage
		fields= ('name', 'email', 'password', 'password_confirm', 'terms_agree')


class SignUpForm(UserCreationForm):
	email= forms.EmailField(help_text= 'Please enter your email')
	secret_word= forms.CharField(help_text= 'This will be used in case we need to verify your identity')

	class Meta:
		model= User
		fields= ('username', 'email', 'password1', 'password2', 'secret_word',)