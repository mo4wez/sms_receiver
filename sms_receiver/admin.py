from django.contrib import admin
from .models import SMS

# Register your models here.
@admin.register(SMS)
class SmsAdmin(admin.ModelAdmin):
    list_display = ['national_code', 'sms_code', 'received_at',]
    ordering = ['-received_at',]