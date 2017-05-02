from django import forms
from .models import SignUp




class ContactForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class signupform(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email', 'name']


	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		#if not domain == 'USC':
		#	raise forms.ValidationError("please add email with USC")
		#if not extension == "edu":
		#	raise forms.ValidationError("please add email with edu")
		return email

	def clean_name(self):
		name = self.cleaned_data.get('name')
		return name