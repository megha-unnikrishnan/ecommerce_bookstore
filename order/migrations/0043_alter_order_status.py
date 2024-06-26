# Generated by Django 4.2.11 on 2024-04-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0042_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Order confirmed', 'Order confirmed'), ('Shipped', 'Shipped'), ('Return processing', 'Return processing'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Cancelled', 'Cancelled'), ('Out for delivery', 'Out for delivery'), ('Return requested', 'Return requested')], default='Order confirmed', max_length=50),
        ),
    ]
