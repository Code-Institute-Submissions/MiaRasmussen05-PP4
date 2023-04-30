from django.contrib import admin

from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Profile)
