# Generated by Django 4.2.11 on 2024-04-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_bookvariant_variant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=150),
        ),
    ]
