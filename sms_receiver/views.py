import re
from datetime import timedelta, timezone, datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SMS
from .serializers import SMSSerializer

from datetime import timedelta, timezone, datetime


@api_view(['GET'])
def get_latest_sms_code(request, national_code):
    sms = SMS.objects.filter(national_code=national_code).order_by('-received_at').first()
    if sms and sms.sms_code and sms.is_valid():
        return Response({
            'status': 'success',
            'sms_code': sms.sms_code
        }, status=200)
    return Response({
        'status': 'failed',
        'message': 'No valid SMS code available.'
    }, status=404)

@api_view(['POST'])
def receive_sms_code(request, national_code):
    # For receiving a new SMS
    bank_message = request.data.get('sms_code')

    # Extract the 6-digit code from the message
    match = re.search(r'\b\d{6}\b', bank_message)
    if match:
        sms_code = match.group(0)  # Extract the matched 6-digit code
        SMS.objects.create(national_code=national_code, sms_code=sms_code, received_at=datetime.now(timezone.utc))
        return Response({'status': 'success'}, status=201)

    return Response({'status': 'failed', 'message': 'No valid 6-digit SMS code found.'}, status=400)
