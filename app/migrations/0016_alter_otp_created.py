# Generated by Django 4.2.3 on 2023-09-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_otp_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]