# Generated by Django 5.2 on 2025-04-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, help_text="Customer's phone number", max_length=20, null=True),
        ),
    ]
