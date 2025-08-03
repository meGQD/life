from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import permission_classes ,api_view
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

            return redirect('home')
        
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
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Account created successfully. You can log in now.')
            return redirect('/auth/login/')
        else:
            for field,errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, error)
    
    return render(request, 'core/signup.html')
