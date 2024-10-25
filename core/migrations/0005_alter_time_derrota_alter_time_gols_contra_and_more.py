# Generated by Django 5.1.1 on 2024-10-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_timejogador_jogador"),
    ]

    operations = [
        migrations.AlterField(
            model_name="time",
            name="derrota",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="time",
            name="gols_contra",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="time",
            name="gols_pro",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="time",
            name="pontos",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="time",
            name="vitoria",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
