from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SMS
from .serializers import SMSSerializer
import re

@api_view(['POST'])
def receive_sms(request):
    """
    Receives an SMS from the forwarder app and saves the verification code
    """
    serializer = SMSSerializer(data=request.data)

    if serializer.is_valid():
        # Save the message
        sms_instance = serializer.save()

        # Extract the SMS code from the message (assuming it's a 6-digit code)
        match = re.search(r'\b\d{6}\b', sms_instance.message)
        if match:
            sms_instance.sms_code = match.group(0)
            sms_instance.save()
            return Response({
                'status': 'success',
                'message': 'SMS code received and saved.',
                'sms_code': sms_instance.sms_code
            }, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'failed',
            'message': 'No valid SMS code found.'
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_latest_sms_code(request):
    """
    Returns the latest SMS code
    """
    sms = SMS.objects.order_by('-received_at').first()
    if sms and sms.sms_code:
        return Response({
            'status': 'success',
            'sms_code': sms.sms_code
        })
    return Response({
        'status': 'failed',
        'message': 'No SMS code available.'
    }, status=404)
