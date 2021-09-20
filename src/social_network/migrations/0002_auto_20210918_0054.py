# Generated by Django 3.2.7 on 2021-09-17 21:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_network', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_updates',
            new_name='date_updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('author', 'title')},
        ),
    ]
