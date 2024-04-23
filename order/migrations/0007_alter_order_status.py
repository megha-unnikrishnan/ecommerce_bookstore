# Generated by Django 4.2.11 on 2024-04-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Return requested', 'Return requested'), ('Order confirmed', 'Order confirmed'), ('Returned', 'Returned'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Return processing', 'Return processing')], default='Order confirmed', max_length=50),
        ),
    ]
