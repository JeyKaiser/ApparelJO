# Generated by Django 4.2 on 2024-09-08 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costeo_app', '0003_rename_proyecto_tasks_proyecto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='proyecto_id',
            new_name='proyecto',
        ),
    ]
