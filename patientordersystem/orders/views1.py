# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Customer, Order
# from .serializers import CustomerSerializer, OrderSerializer
# from rest_framework.permissions import IsAuthenticated
# # View for adding a new customer
# from django.contrib.auth.decorators import login_required

# from authlib.integrations.django_client import OAuth
# from django.shortcuts import redirect
# from django.conf import settings
# from django.http import JsonResponse
# from rest_framework_simplejwt.tokens import AccessToken
# from rest_framework.permissions import AllowAny


# # views.py
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.hashers import make_password
# from django.views.decorators.csrf import csrf_exempt
# from .models import User
# import json

# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')
#         user = User.objects.create(email=email, password=make_password(password))
#         return JsonResponse({'message': 'User registered successfully'}, status=201)

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user:
#             login(request, user)
#             return JsonResponse({'message': 'Logged in successfully'}, status=200)
#         return JsonResponse({'error': 'Invalid credentials'}, status=400)

# @login_required
# def logout_view(request):
#     logout(request)
#     return JsonResponse({'message': 'Logged out successfully'}, status=200)





# # Initialize Auth0 OAuth client
# # oauth = OAuth()
# # oauth.register(
# #     'auth0',
# #     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
# #     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
# #     authorize_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['authorize_url'],
# #     access_token_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['access_token_url'],
# #     userinfo_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['userinfo_url'],
# # )

# # # Login view
# # def login(request):
# #     redirect_uri = 'http://localhost:8000/oidc/callback/'
# #     return oauth.auth0.authorize_redirect(request, redirect_uri)

# # # Callback view to handle response from Auth0
# # def callback(request):
# #     token = oauth.auth0.authorize_access_token(request)
# #     user_info = oauth.auth0.userinfo(token=token)
# #     # Store user info or token in the session, if necessary
# #     request.session['user'] = user_info
# #     return redirect('/')

# oauth = OAuth()
# # oauth.register(
# #     'auth0',
# #     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
# #     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
# #     server_metadata_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['server_metadata_url'],
# #     client_kwargs={
# #         'scope': settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_kwargs']['scope'],
# #     }
# # )

# # oauth.register(
# #     'auth0',
# #     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
# #     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
# #     server_metadata_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['server_metadata_url'],
# #     client_kwargs={
# #         'scope': 'openid profile email',
# #         'audience': settings.SIMPLE_JWT['AUDIENCE'],  # Explicitly set audience here
# #     }
# # )
# OIDC_OP_DOMAIN = "dev-ytcq356n3j8xg643.eu.auth0.com"
# # oauth.register(
# #     'auth0',
# #     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
# #     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
# #     authorize_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['authorize_url'],
# #     access_token_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['access_token_url'],
# #     userinfo_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['userinfo_url'],
# #     jwks_uri=f"https://{OIDC_OP_DOMAIN}/.well-known/jwks.json",
# # )
# oauth.register(
#     'auth0',
#     client_id=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_id'],
#     client_secret=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['client_secret'],
#     authorize_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['authorize_url'],
#     access_token_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['access_token_url'],
#     userinfo_url=settings.AUTHLIB_OAUTH_CLIENTS['auth0']['userinfo_url'],
#     jwks_uri=f"https://{OIDC_OP_DOMAIN}/.well-known/jwks.json",
#     client_kwargs={
#         'scope': 'openid profile email',
#         # 'audience': settings.SIMPLE_JWT['AUDIENCE'],  # Explicitly set audience here
#         'audience': 'https://patientorder.com/api/v3/',
#     }
# )
# # Login view
# def login(request):
#     redirect_uri = 'http://localhost:8000/oidc/callback/'
#     return oauth.auth0.authorize_redirect(request, redirect_uri)

# # Callback view to handle response from Auth0
# # def callback(request):
# #     token = oauth.auth0.authorize_access_token(request)
# #     user_info = oauth.auth0.userinfo(token=token)
# #     # Store user info or token in the session, if necessary
# #     request.session['user'] = user_info
# #     return redirect('/')
# # def callback(request):
# #     token = oauth.auth0.authorize_access_token(request)
# #     user_info = oauth.auth0.userinfo(token=token)

# #     # Save user info and token in session, if necessary
# #     request.session['user'] = user_info
# #     request.session['token'] = token
   

# #     # tokentest = AccessToken(token)
# #     # print(tokentest.payload)
# #     # Temporarily return token for testing purposes
# #     return JsonResponse({
# #         "access_token": token.get("access_token"),
# #         "id_token": token.get("id_token"),
# #         "token_type": token.get("token_type"),
# #         "expires_in": token.get("expires_in"),
# #     })
# # curl --request POST \
# #   --url https://dev-ytcq356n3j8xg643.eu.auth0.com/oauth/token \
# #   --header 'content-type: application/json' \
# #   --data '{"client_id":"loHB9FWuTUICrN5iIhY2O1MZSwcK93KX","client_secret":"DdXWvsuXt9i4jJp7Y15quX2WSDauqP18cAXG_S30ZOnp8nJRyYNmPorpTMGH6wDo","audience":"https://patientorder.com/api/v3/","grant_type":"client_credentials"}'
# def callback(request):
#     token = oauth.auth0.authorize_access_token(request)
#     user_info = oauth.auth0.userinfo(token=token)
#     request.session['user'] = user_info
#     request.session['token'] = token
    
#     # Test output of the token payload to verify 'aud' and 'sub' claims
#     return JsonResponse({
#         "access_token": token.get("access_token"),
#         "id_token": token.get("id_token"),
#         "token_type": token.get("token_type"),
#         "expires_in": token.get("expires_in"),
#         "token_payload": token.get("id_token") or token.get("access_token")
#     })
# # Logout view
# def logout(request):
#     request.session.clear()
#     return redirect('https://dev-ytcq356n3j8xg643.eu.auth0.com/v2/logout?client_id=loHB9FWuTUICrN5iIhY2O1MZSwcK93KX&returnTo=http://localhost:8000/')

# class AddCustomerView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ListCustomersView(APIView):
    
#     def get(self, request):
#         customers = Customer.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)

# class AddOrderView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# class ListOrderView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
