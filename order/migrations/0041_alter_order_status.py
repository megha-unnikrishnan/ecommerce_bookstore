# Generated by Django 4.2.11 on 2024-04-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0040_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Return processing', 'Return processing'), ('Cancelled', 'Cancelled'), ('Out for delivery', 'Out for delivery'), ('Return requested', 'Return requested'), ('Returned', 'Returned'), ('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped')], default='Order confirmed', max_length=50),
        ),
    ]
