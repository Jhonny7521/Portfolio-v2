# Generated by Django 4.1.4 on 2022-12-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_alter_sidevisits_city_alter_sidevisits_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidevisits',
            name='city',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sidevisits',
            name='country',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sidevisits',
            name='country_code',
            field=models.CharField(default='', max_length=5, null=True),
        ),
    ]
