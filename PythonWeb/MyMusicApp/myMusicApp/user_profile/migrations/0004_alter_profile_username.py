# Generated by Django 4.1.2 on 2022-10-05 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('^\\w+$', message='Ensure this value contains only letters, numbers, and underscore.')]),
        ),
    ]
