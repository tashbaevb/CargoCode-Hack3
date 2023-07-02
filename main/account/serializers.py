import base64
from rest_framework import serializers
from .models import Driver, Company
from django.contrib.auth.models import User
from django.core.files.base import ContentFile


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Driver
        fields = (
            'id', 'user', 'driver_license', 'straxovka', 'car_number', 'car_color', 'car_title', 'car_year', 'car_type',
            'bank')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)

        driver_license_file = validated_data.pop('driver_license')
        straxovka_file = validated_data.pop('straxovka')

        driver_license_data = base64.b64decode(driver_license_file)
        straxovka_data = base64.b64decode(straxovka_file)

        driver_license = ContentFile(driver_license_data, name='driver_license')
        straxovka = ContentFile(straxovka_data, name='straxovka')

        driver = Driver.objects.create(user=user, driver_license=driver_license, straxovka=straxovka, **validated_data)
        return driver


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Company
        fields = ('id', 'user', 'company_name', 'company_address', 'descriptions', 'bank_account', 'dot_number')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        company = Company.objects.create(user=user, **validated_data)
        return company


# ------------------------------------------------------------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data['username'],
#             validated_data['email'],
#             validated_data['password']
#         )
#         user.role = 'user'
#         user.save()
#         return user
