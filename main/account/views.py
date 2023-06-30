from rest_framework import generics
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, DriverRegistrationSerializer, CompanyRegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

User = get_user_model()


class DriverRegistrationView(APIView):
    def post(self, request):
        serializer = DriverRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Создание и сохранение водителя
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            driver_license = serializer.validated_data['driver_license']
            # Сохраните другие данные водителя в соответствующей модели
            # ...
            return Response({'message': 'Driver registration successful.'})
        return Response(serializer.errors, status=400)


class CompanyRegistrationView(APIView):
    def post(self, request):
        serializer = CompanyRegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Проверяем роль пользователя
            if request.user.role != 'company':
                return Response({'error': 'Only users with role "company" can register drivers.'}, status=403)

            # Логика регистрации компании
            return Response({'message': 'Company registration successful.'})
        return Response(serializer.errors, status=400)


class CarAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


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


# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
