# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 18:09
from __future__ import unicode_literals

from django.db import migrations

from movieratings.models import Rater


def load_data(*args):
    with open("/Users/BenjaminGHigh/PycharmProjects/bens_movie_ratings/movieratings/migrations/u.user") as users:
        for user in users.readlines():
            Rater.objects.create(user_id=user.split("|")[0], age=user.split("|")[1],
                                 gender=user.split("|")[2], occupation=user.split("|")[3],
                                 zip_code=user.split("|")[4])


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(load_data)
    ]
