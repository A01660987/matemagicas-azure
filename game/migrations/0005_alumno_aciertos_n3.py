# Generated by Django 4.1.7 on 2023-04-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_grupo_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='aciertos_n3',
            field=models.TextField(default=[]),
        ),
    ]
