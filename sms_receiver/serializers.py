from rest_framework import serializers
from .models import SMS

class SMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMS
        fields = ['national_code', 'phone_number', 'message', 'sms_code', 'received_at']
