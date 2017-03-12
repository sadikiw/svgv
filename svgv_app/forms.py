from django import forms
from models import *
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import authenticate, login

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile;
        fields = ('name', 
                  'image', 
                  'university', 
                  'discipline', 
                  'skill_one', 
                  'skill_two',
                  'skill_three',
                  'language_prof', 
                  'personal_site',
                  'exp_one_title',
                  'exp_one',
                  'exp_two_title',
                  'exp_two',
                  'exp_three_title',
                  'exp_three');


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile;
        fields = ('name', 
                  'image', 
                  'product_name', 
                  'product_desc', 
                  'valuation', 
                  'industry',
                  'summary',
                  'ceo', 
                  'company_url');

class CreateUserForm(forms.Form):
    username = forms.CharField(label="Email", required=True, max_length=50)
    password = forms.CharField(label="Password", required=True, max_length=20, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", required=True, max_length=20, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user = CustomUser.objects.filter(username=username)
        if user:
            raise forms.ValidationError("Sorry, this user already exists. Please try again.")
        if password != confirm_password:
            raise forms.ValidationError("Sorry, your passwords don't match. Please try again.")
        return self.cleaned_data


    def create(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user, created = CustomUser.objects.get_or_create(username=username, email=username)
        return (user, created)

    def save(self, user, is_company):
        user.is_company = is_company
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
