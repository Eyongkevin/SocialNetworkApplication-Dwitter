from django.contrib.auth.models import Group
from django.contrib import admin

# Register your models here.
admin.site.unregister(Group)