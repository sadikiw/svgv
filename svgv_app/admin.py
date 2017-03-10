from django.contrib import admin

from .models import *

admin.site.register(CustomUser)
admin.site.register(CompanyProfile)
admin.site.register(UserProfile)