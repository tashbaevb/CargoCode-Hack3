from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, DriverRegistrationAPI, CompanyRegistrationAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/driver/register/', DriverRegistrationAPI.as_view(), name='driver_register'),
    path('api/company/register/', CompanyRegistrationAPI.as_view(), name='company_register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

