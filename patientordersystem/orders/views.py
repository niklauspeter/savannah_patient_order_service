from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
# View for adding a new customer
from django.contrib.auth.decorators import login_required

from authlib.integrations.django_client import OAuth
from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny
from patientordersystem.utils import send_sms
from django.views.decorators.csrf import csrf_exempt 

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AuthenticatedHomeView(TemplateView):
    template_name = 'home_authenticated.html'

def logout_view(request):
    # Clear session and redirect to HomeView
    request.session.clear()
    return redirect(settings.LOGOUT_REDIRECT_URL)

def logout(request):
    request.session.clear()
    return redirect('https://dev-ytcq356n3j8xg643.eu.auth0.com/v2/logout?client_id=loHB9FWuTUICrN5iIhY2O1MZSwcK93KX&returnTo=http://localhost:8000/')

def sendtrialmessage(request):
    send_sms("+254700206386", "Test message from Africa's Talking!")
    return redirect('/')



@csrf_exempt
class AddCustomerView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCustomersView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
@csrf_exempt
class AddOrderView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            customer_phone = order.customer_phone
            message = f"Thank you for your order #{order.id}. {order.item} - KSH {order.amount}. We’ll notify you when it’s ready!"
            send_sms(customer_phone, message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ListOrderView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
