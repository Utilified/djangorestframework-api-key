# Generated by Django 2.2.1 on 2019-05-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_api_key', '0002_apikey_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikey',
            name='has_expired',
            field=models.BooleanField(default=False),
        ),
    ]
