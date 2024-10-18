from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework.views import APIView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from djoser.views import UserViewSet
from rest_framework.decorators import permission_classes ,api_view
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from .permissions import IsNotAuthenticated

@api_view(['POST', 'GET'])
@permission_classes([IsNotAuthenticated])
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 

            return redirect('http://127.0.0.1:8000')
        
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/auth/entry/') 

@api_view(['GET', 'POST'])
@permission_classes([IsNotAuthenticated])
def signup_view(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        messages.success(request, 'Account created successfully. You can log in now.')
        return redirect('/auth/login/')

    return render(request, 'core/signup.html')

# @api_view(['GET', 'POST'])
# @permission_classes([IsNotAuthenticated])
# def signup_view(request):
#     if request.method == 'POST':
#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             messages.success(request, 'Account created successfully. You can log in now.')
#             return redirect('/auth/login/')
#         else:
#             messages.error(request)
    
#     return render(request, 'core/signup.html')
