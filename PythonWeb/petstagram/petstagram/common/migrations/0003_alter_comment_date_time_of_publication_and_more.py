# Generated by Django 4.1.1 on 2022-10-10 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo_alter_photo_tagged_pets'),
        ('common', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time_of_publication',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
        migrations.AlterField(
            model_name='like',
            name='to_photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
    ]