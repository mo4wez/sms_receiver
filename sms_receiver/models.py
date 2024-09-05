from django.db import models

class SMS(models.Model):
    national_code = models.CharField(max_length=10, primary_key=True)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    sms_code = models.CharField(max_length=6, null=True, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS from {self.phone_number} (National Code: {self.national_code})"
