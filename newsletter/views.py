# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm, signupform
from .models import SignUp
# Create your views here.

def home(request):
	title = "Sign up"
	form = signupform(request.POST or None)
	context = {
		"title" : title,
		"form" : form
	}	

	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
			"title" : "Thank You"
		}

	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset" : queryset
		}

	
	return render(request, "home.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	title = "Contact Form"
	context = {
		"form" : form,
		"title" :  title
	}

	if form.is_valid():
		form_name = form.cleaned_data.get("name")
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		send_mail(
			'its working',
			'Welcome.',
			'jakharaman1996@outlook.com',
			['jakharaman@yahoo.com'],
			fail_silently=False,
			)

	return render(request, "form.html", context)








