# Generated by Django 4.2.3 on 2023-09-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_spam'),
    ]

    operations = [
        migrations.AddField(
            model_name='spam',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]