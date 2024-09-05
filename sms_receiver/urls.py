from django.urls import path
from .views import receive_sms, get_latest_sms_code

urlpatterns = [
    path('receive-sms/', receive_sms, name='receive_sms'),
    path('<str:national_code>/', get_latest_sms_code, name='get_latest_sms_code'),
]
