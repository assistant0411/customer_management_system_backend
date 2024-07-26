# Generated by Django 4.2.7 on 2024-07-18 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_budget_job_original_image_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='original_image_url',
            new_name='charge_original_image_url',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='result_image_url',
            new_name='charge_result_image_url',
        ),
        migrations.AddField(
            model_name='job',
            name='estimate_original_image_url',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='job',
            name='estimate_result_image_url',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]