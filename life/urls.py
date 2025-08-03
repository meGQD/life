from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.me, name='me'),
    path('remainingWeeks/', views.remaining_weeks, name='remainingWeeks'),
    path('customers/', views.customers),
]