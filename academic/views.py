# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from .forms import NewOrderForm
from .models import OrderJob
from regsignup.models import Profile

# Create your views here.
def login(request):
	context = {}
	return render(request, 'academic/sign_in.html', context)

@login_required
def dashboard(request):
 	context= {}
 	return render(request, 'academic/index.html', context)

def current_orders(request):
	papers= OrderJob.objects.filter(created_date__lte= timezone.now()).order_by('id')
	context= {'papers': papers}
	return render(request, 'academic/current_orders.html', context)

def revisions(request):
	context = {}
	return render(request, 'academic/revisions.html', context)

def approved_orders(request):
	context= {}
	return render(request, 'academic/approved_orders.html', context)

def payment_history(request):
	context= {}
	return render(request, 'academic/payment_history.html', context)


def invoice(request):
	posters= OrderJob.objects.filter(created_date__lte= timezone.now()).order_by('order_num')
	#OrderJob.pk
	#costs = get_object_or_404(OrderJob, pk)
	#context= {'costs': costs}
	context={}
	return render(request, 'academic/invoice.html', context)

def new_order(request):
	if request.method == "POST":
		form = NewOrderForm(request.POST)
		if form.is_valid():
			kazi= form.save(commit= False)
			kazi.created_date= timezone.now()
			#kazi.paper_cost= total()
			kazi.save
			return redirect('invoice')
	else:
		form= NewOrderForm()
	context= {'form': form}
	return render(request, 'academic/order_new.html', context)

def order(request, pk):
	papers= get_object_or_404(OrderJob, pk=pk)
	context = {'papers': papers}
	return render(request, 'academic/order.html', context)

