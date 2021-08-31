# Generated by Django 3.2 on 2021-06-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_order_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ref_id',
            field=models.ManyToManyField(related_name='ref_id', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_ref',
            field=models.CharField(default='716E9A56F661', editable=False, max_length=12),
        ),
    ]
