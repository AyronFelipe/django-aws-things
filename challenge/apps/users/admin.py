from django.contrib import admin

from challenge.apps.users.models import UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    pass
