from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from .models import *
from .forms import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def CreateCompanyProfile(request):
    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_prof = form.save(commit=False)
            user_prof.username = request.user.username
            user_prof.image = request.FILES['image']
            user_prof.save()
    else:
        form = CompanyProfileForm();
    return render(request, 'svgv_app/company_form.html', {'form': form})

def CreateUserProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_prof = form.save(commit=False)
            uni = '.' + user_prof.university.lower().replace(' ', '-')
            user_prof.uni_class = uni
            user_prof.username = request.user.username
            user_prof.image = request.FILES['image']
            user_prof.save()
    else:
        form = UserProfileForm();
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

def create_company(request):
    return create_user(request, True)

def create_member(request):
    return create_user(request, False)

# def login_user(request):

def create_user(request, is_company):
    template = 'svgv_app/create_user.html' 
    next_template = 'userform'
    if is_company:
        template = 'svgv_app/create_company.html'     
        next_template = 'companyform'  

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user, created = form.create(request)
            if created:
                user = form.save(user, is_company)
                user = form.login(request)
                if user:
                    login(request, user)
                    return HttpResponseRedirect(reverse(next_template))
    else:
        form = CreateUserForm()
    return render(request,template, {'form': form})
