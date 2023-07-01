from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

COLOR_CAR = (
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black')
)

TYPE_OF_CAR = (
    ('big', 'big'),
    ('middle', 'middle'),
    ('minivan', 'minivan')
)


class Driver(models.Model):
    driver_license = models.FileField(upload_to='')
    straxovka = models.FileField(upload_to='')
    car_number = models.CharField(max_length=50)
    car_color = models.CharField(choices=COLOR_CAR, max_length=50, null=True)
    car_title = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_type = models.CharField(choices=TYPE_OF_CAR, max_length=30)
    bank = models.CharField(max_length=100)


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    number_of_driver = models.IntegerField()
    descriptions = models.TextField(max_length=1000)
    bank_account = models.CharField(max_length=100)


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('driver', 'Driver'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_set',
                                    related_query_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True,
                                              related_name='custom_user_set', related_query_name='custom_user')
