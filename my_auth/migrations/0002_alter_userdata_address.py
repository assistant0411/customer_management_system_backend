# Generated by Django 4.2.7 on 2024-01-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
