# from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.hashers import make_password
# from django.http import JsonResponse
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