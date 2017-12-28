from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.forms import ModelForm
import datetime

# Create your models here.

SUBJECT_CHOICES= (
	('Accounting', 'Accounting'),
	('Biology', 'Biology'),
	('Chemistry', 'Chemistry'),
	)

STYLE_CHOICES= (
	('APA', 'APA'),
	('MLA', 'APA'),
	('Harvard', 'Harvard'),
	('Chicago', 'Chicago'),
	('Turabian', 'Turabian'),
	('Oxford', 'Oxford'),
	('AMA', 'AMA'),
	('Bluebook', 'Bluebook'),
	('Others','Others'),
	)

class OrderJob(models.Model):
	#order_num= models.IntegerField()
	#client_num= models.ForeignKey()
	order_pages= models.IntegerField()
	paper_subject= models.CharField(max_length=50, choices= SUBJECT_CHOICES)
	paper_topic= models.CharField(max_length= 150)
	paper_style= models.CharField(max_length= 15, choices= STYLE_CHOICES)
	sources_num= models.IntegerField()
	paper_deadline= models.IntegerField()
	paper_cost= models.IntegerField(default= 0)
	paper_instruc= models.TextField(max_length= 2000)
	paper_files= models.FileField(blank=True)
	created_date = models.DateTimeField(
		default = timezone.now)
	#due_date= models.DateTimeField(blank=False)

	def price_calc(self):
		#print("test price_calc")
		if self.paper_deadline <= 12:
			unit_cost = 35
		elif self.paper_deadline >= 12 <= 24:
			unit_cost= 30
		elif self.paper_deadline >= 25 <= 36:
			unit_cost= 25
		else:
			unit_cost= 20
		return unit_cost * self.order_pages
		#print("test Here")
		paper_cost= price_calc()

	def __str__(self):
		return self.paper_topic
		
	paper_cost= price_calc

class Messages():
	msg_sender= models.ForeignKey(User)
	msg_recipient= models.ForeignKey(User)
	msg_send_date= models.DateTimeField(default= timezone.now)
	msg_content= models.TextField(max_length=2000, blank= False)






		








