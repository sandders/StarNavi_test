# Generated by Django 3.2.7 on 2021-09-21 22:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_request',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 22, 1, 34, 2, 291229, tzinfo=utc), verbose_name='last request'),
        ),
    ]
