from django.urls import path
from .views import get_latest_sms_code, receive_sms_code

urlpatterns = [
    path('<str:national_code>/', get_latest_sms_code, name='get_latest_sms_code'),
    path('receive/<str:national_code>/', receive_sms_code, name='receive_sms_code'),
]
