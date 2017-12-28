# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	name = models.CharField(max_length= 30, blank=True)
	email= models.EmailField(max_length=100, blank=False, default='ab@cd.com')
	secret_word= models.CharField(max_length=10, blank=False, default= 'secret')



@receiver(post_save, sender= User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user= instance)
	instance.profile.save()

class UserCreationForm(models.Model):
	name = models.CharField(max_length=250)
	email= models.EmailField(max_length=250, blank=False)
	password= models.CharField(max_length=250, blank=False)
	published_date = models.DateTimeField(
		    blank= True, null= True)

	def publish(self):
		self.published_date= timezone.now()
		self.save()

	def __str__(self):
		return self.title

class SignupPage(models.Model):
	name= models.CharField(max_length=350)
	email= models.EmailField(max_length=250, blank=False)
	password=models.CharField(max_length=100, blank=False)
	password_confirm= models.CharField(max_length=100, blank= False)
	signup_date= models.DateTimeField(default=timezone.now)
	terms_agree=models.BooleanField(max_length=15, blank= False)

	def publish(self):
		self.signup_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class SignIn(models.Model):
	email= models.EmailField(max_length=250, blank=False)
	password= models.CharField(max_length=100, blank=False)
	




