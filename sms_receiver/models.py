from django.db import models

class SMS(models.Model):
    national_code = models.CharField(max_length=10, unique=False)
    sms_code = models.CharField(max_length=10)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SMS for {self.national_code} - Code: {self.sms_code}'

