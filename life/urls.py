from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from rest_framework_nested import routers
from . import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('remainingWeeks/', views.remaining_weeks, name='remainingWeeks'),
    path('customers/', views.customers),
]