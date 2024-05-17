# Generated by Django 4.2.11 on 2024-05-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0049_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Shipped', 'Shipped'), ('Out for delivery', 'Out for delivery'), ('Return requested', 'Return requested'), ('Cancelled', 'Cancelled'), ('Return processing', 'Return processing'), ('Returned', 'Returned'), ('Delivered', 'Delivered'), ('Order confirmed', 'Order confirmed')], default='Order confirmed', max_length=50),
        ),
    ]