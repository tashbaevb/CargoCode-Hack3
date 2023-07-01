from rest_framework import serializers
from .models import Company, Driver
from django.contrib.auth.models import User


#
# class DriverRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Driver
#         fields = (
#             'id', 'driver_license', 'straxovka', 'car_number', 'car_color', 'car_title', 'car_year', 'car_type', 'bank',
#             'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
#         user.role = 'driver'
#         user.save()
#         driver = Driver.objects.create(user=user, driver_license=validated_data['driver_license'],
#                                        straxovka=validated_data['straxovka'], car_number=validated_data['car_number'],
#                                        car_color=validated_data['car_color'], car_title=validated_data['car_title'],
#                                        car_year=validated_data['car_year'], car_type=validated_data['car_type'],
#                                        bank=validated_data['bank'])
#         return driver

# Driver Serializer
class DriverRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('driver_license', 'straxovka', 'car_number', 'car_color', 'car_title', 'car_year', 'car_type', 'bank')


class CompanyRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'company_address', 'number_of_driver', 'descriptions', 'bank_account')


# ------------------------------------------------------------------------------------

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
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
