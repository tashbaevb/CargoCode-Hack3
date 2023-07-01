from django.db import models
from django.contrib.auth.models import User

TYPE_OF_CAR = (
    ('big', 'big'),
    ('middle', 'middle'),
    ('minivan', 'minivan')
)


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    driver_license = models.FileField(max_length=100)
    straxovka = models.FileField(max_length=100)
    car_number = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_type = models.CharField(choices=TYPE_OF_CAR, max_length=100)
    bank = models.CharField(max_length=100)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    number_of_driver = models.IntegerField()
    descriptions = models.TextField()
    bank_account = models.CharField(max_length=100)
