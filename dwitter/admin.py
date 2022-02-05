from django.contrib.auth.models import Group, User
from django.contrib import admin

from dwitter import models


class UserAdmin(admin.ModelAdmin):
    fields = ['username']


# Unregister your models here
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(models.Profile)