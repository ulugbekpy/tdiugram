# Generated by Django 4.1.7 on 2023-03-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_foydalanuvchi'),
    ]

    operations = [
        migrations.AddField(
            model_name='foydalanuvchi',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]