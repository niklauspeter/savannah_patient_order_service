import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms(recipient, message):
    try:
        response = sms.send(message, [recipient])
        print(response)
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None
