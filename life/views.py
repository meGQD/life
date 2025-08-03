from datetime import date
from django.shortcuts import render
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer

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
    messages.error(request, "You dont have permission G")
    return render(request, 'life/home.html')

