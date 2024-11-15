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

# Initialize Auth0 OAuth client
# oauth = OAuth()
# oauth.register(
#     'auth0',
#     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
#     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
#     authorize_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['authorize_url'],
#     access_token_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['access_token_url'],
#     userinfo_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['userinfo_url'],
# )

# # Login view
# def login(request):
#     redirect_uri = 'http://localhost:8000/oidc/callback/'
#     return oauth.auth0.authorize_redirect(request, redirect_uri)

# # Callback view to handle response from Auth0
# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     user_info = oauth.auth0.userinfo(token=token)
#     # Store user info or token in the session, if necessary
#     request.session['user'] = user_info
#     return redirect('/')

oauth = OAuth()
oauth.register(
    'auth0',
    client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
    client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
    server_metadata_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['server_metadata_url'],
    client_kwargs={
        'scope': settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_kwargs']['scope'],
    }
)

# Login view
def login(request):
    redirect_uri = 'http://localhost:8000/oidc/callback/'
    return oauth.auth0.authorize_redirect(request, redirect_uri)

# Callback view to handle response from Auth0
# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     user_info = oauth.auth0.userinfo(token=token)
#     # Store user info or token in the session, if necessary
#     request.session['user'] = user_info
#     return redirect('/')
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    user_info = oauth.auth0.userinfo(token=token)

    # Save user info and token in session, if necessary
    request.session['user'] = user_info
    request.session['token'] = token

    # Temporarily return token for testing purposes
    return JsonResponse({
        "access_token": token.get("access_token"),
        "id_token": token.get("id_token"),
        "token_type": token.get("token_type"),
        "expires_in": token.get("expires_in"),
    })

# Logout view
def logout(request):
    request.session.clear()
    return redirect('https://dev-ytcq356n3j8xg643.eu.auth0.com/v2/logout?client_id=loHB9FWuTUICrN5iIhY2O1MZSwcK93KX&returnTo=http://localhost:8000/')

class AddCustomerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCustomersView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class AddOrderView(APIView):

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ListOrderView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
