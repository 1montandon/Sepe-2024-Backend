# Generated by Django 5.1.1 on 2024-12-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_jogo_jogo_realizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='tipo_jogo',
            field=models.CharField(choices=[('Grupo', 'Grupo'), ('Semi', 'Semi'), ('Final', 'Final')], default='Grupo', max_length=5),
        ),
    ]