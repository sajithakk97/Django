# Generated by Django 3.2.25 on 2025-01-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20250102_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
