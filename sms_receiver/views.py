from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SMS
from .serializers import SMSSerializer
import re

@api_view(['POST'])
def receive_sms(request):
    """
    Receives an SMS via POST and stores it in the database.
    Expects 'national_code' and 'sms_code' in the POST data.
    """
    national_code = request.data.get('national_code')
    sms_code = request.data.get('sms_code')

    if not national_code or not sms_code:
        return Response({'status': 'failed', 'message': 'national_code or sms_code missing'}, status=400)

    # Save the SMS to the database
    sms = SMS.objects.create(national_code=national_code, sms_code=sms_code)
    return Response({'status': 'success', 'message': 'SMS received and saved successfully.'})

@api_view(['GET'])
def get_latest_sms_code(request, national_code):
    """
    Returns the latest SMS code for the given national code.
    """
    sms = SMS.objects.filter(national_code=national_code).order_by('-received_at').first()
    if sms:
        return Response({
            'status': 'success',
            'sms_code': sms.sms_code
        })
    return Response({
        'status': 'failed',
        'message': 'No SMS code available for this national code.'
    }, status=404)