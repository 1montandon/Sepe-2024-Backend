# Generated by Django 5.1.1 on 2024-12-17 13:48

import core.models.user
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', core.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('numero', models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('posicao', models.CharField(choices=[(1, 'Goleiro'), (2, 'Fixo'), (3, 'Ala'), (4, 'Pivo')], max_length=10)),
                ('foto', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader.image')),
            ],
        ),
        migrations.CreateModel(
            name='Rodada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_rodada', models.IntegerField()),
                ('campeonato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rodada', to='core.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('gols_pro', models.IntegerField(blank=True, default=0, null=True)),
                ('gols_contra', models.IntegerField(blank=True, default=0, null=True)),
                ('vitoria', models.IntegerField(blank=True, default=0, null=True)),
                ('empate', models.IntegerField(blank=True, default=0, null=True)),
                ('derrota', models.IntegerField(blank=True, default=0, null=True)),
                ('pontos', models.IntegerField(blank=True, default=0, null=True)),
                ('campeonato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='time', to='core.campeonato')),
                ('escudo', models.ForeignKey(blank=True, default='https://i.ibb.co/VDwW5Rv/28-289657-espn-soccer-team-logo-default.png', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='uploader.image')),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('horario', models.TimeField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=150, null=True)),
                ('gols', models.JSONField(blank=True, null=True)),
                ('cartoes', models.JSONField(blank=True, null=True)),
                ('tipo_jogo', models.CharField(choices=[('Grupo', 'Grupo'), ('Semi', 'Semi'), ('Final', 'Final')], default='Grupo', max_length=5)),
                ('jogo_realizado', models.BooleanField(default=False)),
                ('rodada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jogos', to='core.rodada')),
                ('time_mandante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jogos_mandante', to='core.time')),
                ('time_visitante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jogos_visitante', to='core.time')),
                ('vencedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='core.time')),
            ],
        ),
        migrations.CreateModel(
            name='TimeJogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='core.jogador')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogadores', to='core.time')),
            ],
        ),
    ]
