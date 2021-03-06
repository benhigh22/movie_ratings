# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0004_auto_20160225_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rater',
            name='id',
        ),
        migrations.AddField(
            model_name='rater',
            name='user_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movieratings.Movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieratings.Rater'),
        ),
    ]
