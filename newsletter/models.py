# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=120, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)


	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email