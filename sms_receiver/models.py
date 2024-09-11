from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class SMS(models.Model):
    national_code = models.CharField(max_length=10, unique=False)
    sms_code = models.CharField(max_length=6)
    received_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural = 'sms codes'


    def is_valid(self):
        expiration_time = self.received_at + timedelta(minutes=2)
        return now() <= expiration_time
    
    def __str__(self):
        return f'SMS for {self.national_code} - Code: {self.sms_code}'

