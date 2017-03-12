from __future__ import unicode_literals
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)

class CompanyProfile(models.Model):
	username = models.CharField(max_length=100, default=None, blank=True)
	name = models.CharField(max_length=100, default=None, blank=True)
	image = models.ImageField(upload_to='company_image/', blank=True, null=True)
	product_name = models.CharField(max_length=100, default=None, blank=True)
	product_desc = models.TextField(blank=True)
	valuation = models.CharField(max_length=50, default=None, blank=True)
	industry = models.CharField(max_length=50, default=None, blank=True)
	summary = models.TextField(blank=True)
	ceo = models.CharField(max_length=50, default=None, blank=True)
	company_url = models.CharField(max_length=100, default=None, blank=True)	

class UserProfile(models.Model):
	username = models.CharField(max_length=100, default=None, blank=True)
	name = models.CharField(max_length=100, default=None, blank=True)
	desc = models.TextField(blank=True)
	image = models.ImageField(upload_to='user_image/', blank=True, null=True)
	university = models.CharField(max_length=100, default=None, blank=True)
	uni_class = models.CharField(max_length=100, default=None, blank=True)
	discipline = models.CharField(max_length=50, default=None, blank=True)
	skill_one = models.CharField(max_length=50, default=None, blank=True)
	skill_two = models.CharField(max_length=50, default=None, blank=True)
	skill_three = models.CharField(max_length=50, default=None, blank=True)
	language_prof = models.CharField(max_length=100, default=None, blank=True)
	personal_site = models.CharField(max_length=100, default=None, blank=True)
	exp_one_title = models.CharField(max_length=50, default=None, blank=True)
	exp_two_title = models.CharField(max_length=50, default=None, blank=True)
	exp_three_title = models.CharField(max_length=50, default=None, blank=True)
	exp_one = models.TextField(blank=True)
	exp_two = models.TextField(blank=True)
	exp_three = models.TextField(blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()


# @receiver(post_save, sender=User)
# def create_company_profile(sender, instance, created, **kwargs):
#     if created:
#         CompanyProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_company_profile(sender, instance, **kwargs):
#     instance.companyprofile.save()

