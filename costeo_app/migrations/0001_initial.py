# Generated by Django 4.2 on 2024-09-30 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aparrel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(blank=True, max_length=30, null=True)),
                ('fotoReferencia', models.CharField(blank=True, max_length=30, null=True)),
                ('codigoSapMD', models.CharField(blank=True, max_length=30, null=True)),
                ('codigoSapPT', models.CharField(blank=True, max_length=30, null=True)),
                ('nombreSistema', models.CharField(blank=True, max_length=30, null=True)),
                ('descripcionColor', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='costeo_app.proyecto')),
            ],
        ),
    ]
