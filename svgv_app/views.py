from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import *
from .forms import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def CreateCompanyProfile(request):
	if request.method == "POST":
		form = CompanyProfileForm(request.POST, request.FILES)
		if form.is_valid():
			user_prof = form.save(commit=False)
			user_prof.username = 'Nathan'
			user_prof.image = request.FILES['image']
			user_prof.save()
	else:
		form = CompanyProfileForm();
	return render(request, 'svgv_app/company_form.html', {'form': form})

def CreateUserProfile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			user_prof = form.save(commit=False)
			user_prof.username = 'Nathan'
			user_prof.image = request.FILES['image']
			user_prof.save()
	else:
		form = CompanyProfileForm();
	return render(request, 'svgv_app/user_form.html', {'form': form})

class CompanyDetailView(generic.DetailView):
	model = CompanyProfile
	template_name = 'svgv_app/company.html'

	def get_queryset(self):
		return CompanyProfile.objects.filter()
	def get_absolute_url(self):
		return reverse('company', kwargs={'pk':self.id})

class UserDetailView(generic.DetailView):
	model = UserProfile
	template_name = 'svgv_app/member.html'

	def get_queryset(self):
		return UserProfile.objects.filter()
	def get_absolute_url(self):
		return reverse('member', kwargs={'pk':self.id})

class CompanyListView(generic.ListView):
	template_name = 'svgv_app/companies.html'
	context_object_name = 'all_companies'

	def get_queryset(self):
		queryset = CompanyProfile.objects.all()
		return queryset

class UserListView(generic.ListView):
	template_name = 'svgv_app/members.html'
	context_object_name = 'all_users'

	def get_queryset(self):
		queryset = UserProfile.objects.all()
		return queryset