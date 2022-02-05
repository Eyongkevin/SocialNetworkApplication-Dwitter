from django.contrib.auth.models import Group, User
from django.contrib import admin

from dwitter import models

class ProfileInLine(admin.StackedInline):
    model = models.Profile


class UserAdmin(admin.ModelAdmin):
    fields = ['username']
    inlines = [ProfileInLine]


# Unregister your models here
admin.site.unregister(Group)
admin.site.unregister(User)

# Register your models here.
admin.site.register(User, UserAdmin)