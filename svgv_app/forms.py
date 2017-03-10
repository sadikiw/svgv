from django import forms
from models import *
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile;
		fields = ('name', 'image', 'university', 'skills', 'language_prof', 'personal_site');


class CompanyProfileForm(forms.ModelForm):
	class Meta:
		model = CompanyProfile;
		fields = ('name', 'image', 'product_name', 'product_desc', 'valuation', 'ceo', 'company_url');

