# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='favorite',
            field=models.IntegerField(default=0, verbose_name='收藏'),
        ),
        migrations.AddField(
            model_name='artical',
            name='thumbsdown',
            field=models.IntegerField(default=0, verbose_name='不支持'),
        ),
        migrations.AddField(
            model_name='artical',
            name='thumbsup',
            field=models.IntegerField(default=0, verbose_name='支持'),
        ),
        migrations.AlterField(
            model_name='artical',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
