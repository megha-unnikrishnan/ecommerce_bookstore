# Generated by Django 4.2.11 on 2024-05-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0046_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Return processing', 'Return processing'), ('Shipped', 'Shipped'), ('Order confirmed', 'Order confirmed'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Returned', 'Returned'), ('Return requested', 'Return requested')], default='Order confirmed', max_length=50),
        ),
    ]