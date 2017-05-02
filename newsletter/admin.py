# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import signupform
from .models import SignUp
# Register your models here.
class signupadmin(admin.ModelAdmin):
	form = signupform
	#class Meta:
	#	model = SignUp
	list_display = ["__unicode__", "timestamp", "update"]




admin.site.register(SignUp, signupadmin)