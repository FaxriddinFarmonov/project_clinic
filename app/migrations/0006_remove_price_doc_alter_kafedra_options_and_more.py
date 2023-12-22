# Generated by Django 4.2.3 on 2023-12-22 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_kafedra_remove_price_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='doc',
        ),
        migrations.AlterModelOptions(
            name='kafedra',
            options={'verbose_name': 'Kafedra', 'verbose_name_plural': '2. Kafedra'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='prof',
        ),
        migrations.RemoveField(
            model_name='user',
            name='prosition',
        ),
        migrations.DeleteModel(
            name='DocTime',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.DeleteModel(
            name='Professions',
        ),
    ]
