# Generated by Django 3.2 on 2021-04-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myinventory', '0002_auto_20210422_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='Employer_job',
            field=models.CharField(choices=[('PRODUCT MANAGER', 'PRODUCTMANAGER'), ('GENERAL MANAGER', 'GENERALMANAGER'), ('DELIVERY', 'DELIVERY')], default='', max_length=200),
        ),
    ]
