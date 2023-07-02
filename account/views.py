from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, CompanySerializer, DriverSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
import base64
from django.core.files.base import ContentFile
from .models import Driver


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class DriverRegisterAPI(generics.GenericAPIView):
    serializer_class = DriverSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        # Получение и кодирование файлов в формат base64
        driver_license_file = request.FILES.get('driver_license')
        straxovka_file = request.FILES.get('straxovka')

        if driver_license_file:
            data['driver_license'] = self.encode_file_to_base64(driver_license_file)

        if straxovka_file:
            data['straxovka'] = self.encode_file_to_base64(straxovka_file)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        driver = serializer.save()
        return Response({
            "driver": DriverSerializer(driver, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(driver.user)[1]
        })

    def encode_file_to_base64(self, file):
        try:
            file_data = file.read()
            encoded_data = base64.b64encode(file_data)
            return encoded_data.decode('utf-8')
        except Exception as e:
            # Обработка ошибки при чтении и кодировании файла
            raise serializers.ValidationError("Ошибка при кодировании файла")


# class DriverRegisterAPI(generics.GenericAPIView):
#     serializer_class = DriverSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         driver = serializer.save()
#         return Response({
#             "driver": DriverSerializer(driver, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(driver.user)[1]
#         })


class CompanyRegisterAPI(generics.GenericAPIView):
    serializer_class = CompanySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        return Response({
            "company": CompanySerializer(company, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(company.user)[1]
        })


# ------------------------------------------------------------------------


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
