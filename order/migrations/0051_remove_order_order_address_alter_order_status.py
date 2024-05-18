# Generated by Django 4.2.11 on 2024-05-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_order_order_address_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_address',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Return requested', 'Return requested'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled'), ('Order confirmed', 'Order confirmed'), ('Return processing', 'Return processing'), ('Delivered', 'Delivered'), ('Shipped', 'Shipped'), ('Out for delivery', 'Out for delivery')], default='Order confirmed', max_length=50),
        ),
    ]
