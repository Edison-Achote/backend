# Generated by Django 5.0.7 on 2024-08-02 00:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CuidadoCultivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('actividades', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Postcosecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('actividades', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PreparacionTerreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Siembra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo_planta', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.cosecha')),
                ('cuidado_cultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.cuidadocultivo')),
                ('postcosecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.postcosecha')),
                ('preparacion_terreno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.preparacionterreno')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('siembra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tareas.siembra')),
            ],
        ),
    ]