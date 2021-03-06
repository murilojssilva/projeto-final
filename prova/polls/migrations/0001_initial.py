# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('idHistorico', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('idOpcao', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('aOpcao', models.CharField(max_length=200)),
                ('bOpcao', models.CharField(max_length=200)),
                ('cOpcao', models.CharField(max_length=200)),
                ('dOpcao', models.CharField(max_length=200)),
                ('eOpcao', models.CharField(max_length=200)),
                ('escolhidaOpcao', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('idProva', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('tipoProva', models.CharField(max_length=5)),
                ('anoProva', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('idQuestao', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('areaQuestao', models.CharField(max_length=50)),
                ('tipoQuestao', models.CharField(max_length=1)),
                ('textoQuestao', models.CharField(blank=True, max_length=500, null=True)),
                ('imagemQuestao', models.ImageField(blank=True, null=True, upload_to='')),
                ('perguntaQuestao', models.CharField(blank=True, max_length=200, null=True)),
                ('statusQuestao', models.CharField(max_length=1)),
                ('idProva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Prova')),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('idResposta', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('tipoResposta', models.CharField(max_length=1)),
                ('certaResposta', models.CharField(max_length=1)),
                ('textoResposta', models.CharField(max_length=1000)),
                ('idQuestao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questao')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('matriculaUsuario', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nomeUsuario', models.CharField(max_length=200)),
                ('tipoUsuario', models.CharField(max_length=1)),
                ('emailUsuario', models.EmailField(max_length=254)),
                ('senhaUsuario', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='resposta',
            name='matriculaUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario'),
        ),
        migrations.AddField(
            model_name='opcao',
            name='idQuestao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questao'),
        ),
        migrations.AddField(
            model_name='historico',
            name='idProva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Prova'),
        ),
        migrations.AddField(
            model_name='historico',
            name='matriculaUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Usuario'),
        ),
    ]
