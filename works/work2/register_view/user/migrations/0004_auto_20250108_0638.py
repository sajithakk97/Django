# Generated by Django 3.2.25 on 2025-01-08 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='upload',
            new_name='image',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
