# Generated by Django 4.2.11 on 2024-04-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookvariant',
            name='product_variant_desc',
            field=models.TextField(null=True),
        ),
    ]
