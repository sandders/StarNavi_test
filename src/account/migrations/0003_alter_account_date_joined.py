# Generated by Django 3.2.7 on 2021-09-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
    ]
