from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('entry/', TemplateView.as_view(template_name='core/entry.html'), name='entry'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]