from knox import views as knox_views
from .views import CarAPIView, RegisterAPI, LoginAPI, DriverRegistrationView, CompanyRegistrationView
from django.urls import path

urlpatterns = [
    path('api/car/', CarAPIView.as_view()),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register/driver/', DriverRegistrationView.as_view(), name='driver-registration'),
    path('register/company/', CompanyRegistrationView.as_view(), name='company-registration'),
]
