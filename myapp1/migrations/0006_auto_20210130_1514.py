# Generated by Django 3.1.5 on 2021-01-30 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_product_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
    ]
