# Generated by Django 4.2.2 on 2023-07-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_driver_car_type_alter_driver_driver_license_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='dot_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_license',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='straxovka',
            field=models.TextField(),
        ),
    ]
