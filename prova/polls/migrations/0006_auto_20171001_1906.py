# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_questao_imagem2questao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='imagem2Questao',
            field=models.FileField(blank=True, null=True, upload_to='static/img/uploads'),
        ),
        migrations.AlterField(
            model_name='questao',
            name='imagemQuestao',
            field=models.FileField(blank=True, null=True, upload_to='static/img/uploads'),
        ),
        migrations.AlterField(
            model_name='questao',
            name='perguntaQuestao',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
