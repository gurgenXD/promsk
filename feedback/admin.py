from django.contrib import admin
from feedback.models import *


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created')


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_or_phone', 'created')