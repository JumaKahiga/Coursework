# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.utils import timezone
from .forms import RegForm, SignUpForm
from .models import UserCreationForm, SignupPage

# Create your views here.

#def signup(request):
	#context = {}
	#return render(request, 'regsignup/register.html', context)



def regsign(request):
	if request.method== "POST":
		form= RegForm(request.POST)
		if form.is_valid():
			client= form.save(commit= False)
			client.signup_date= timezone.now()
			client.save
			return redirect('home')
	else:
		form= RegForm()
	return render(request, 'regsignup/register.html', {'form': form})

def signup(request):
	if request.method=="POST":
		form= SignUpForm(request.POST)
		if form.is_valid():
			user= form.save()
			user.refresh_from_db() #load the profile instance created by the signal
			user.profile.email= form.cleaned_data.get('email')
			user.profile.secret_word= form.cleaned_data('secret_word')
			user.save()
			raw_password= form.cleaned_data.get('password1')
			user= authenticate(username= user.username, password=raw_password)
			login(request, user)
			return redirect('../academic/dashboard')
	else:
		form= SignUpForm()
	return render(request, 'register.html', {'form': form})



