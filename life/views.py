from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from .models import Customer
from .serializers import CustomerSerializer
from .permissions import IsNotLoggedIn
from django.contrib.auth import base_user

@api_view(['GET', 'PUT'])
def me(request):

    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in')
        return render(request, 'life/home.html')

    (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return render(request, 'life/profile.html', { 'customer_details': serializer.data })
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view()
def remaining_weeks(request):

    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in')
        return render(request, 'life/home.html')

    (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)

    passed_weeks = int((date.today() - customer.user.birth_date).days / 7)

    remaining_weeks = int((customer.user.expected_death_date - date.today()).days / 7)

    return render(request, 'life/remainingWeeks.html', { 'passed_weeks': passed_weeks, 'remaining_weeks' : remaining_weeks })

@api_view()
def customers(request):
    if request.user.is_staff:
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    return Response("You dont have permission G")
