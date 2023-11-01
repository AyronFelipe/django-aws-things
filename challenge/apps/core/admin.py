from django.contrib import admin

from challenge.apps.core.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
