# Generated by Django 4.2 on 2024-10-14 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costeo_app', '0003_tipo_alter_collection_descripcioncolor_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tecnicos',
            new_name='Creativo',
        ),
        migrations.RenameModel(
            old_name='Fotos',
            new_name='Foto',
        ),
        migrations.RenameModel(
            old_name='Lineas',
            new_name='Linea',
        ),
        migrations.RenameModel(
            old_name='Creativos',
            new_name='Tecnico',
        ),
        migrations.RenameModel(
            old_name='Telas',
            new_name='Tela',
        ),
        migrations.RenameField(
            model_name='creativo',
            old_name='nombreTecnico',
            new_name='nombreCreativo',
        ),
        migrations.RenameField(
            model_name='tecnico',
            old_name='nombreCreativo',
            new_name='nombreTecnico',
        ),
    ]
