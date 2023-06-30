from rest_framework import serializers, viewsets
from .models import Car, Company
from django.contrib.auth.models import User


class DriverRegistrationSerializer(serializers.Serializer):
    # Поля для регистрации водителя



class CompanyRegisterSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(write_only=True)
    company_address = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'company_name', 'company_address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.role = 'company'
        user.save()

        company = Company.objects.create(
            user=user,
            company_name=validated_data['company_name'],
            company_address=validated_data['company_address']
        )

        return user


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='user')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        user.role = validated_data['role']
        user.save()
        return user


#
# # Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         user.role = 'user'
#         user.save()
#         return user
