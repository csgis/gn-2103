# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geonode_themes', '0008_auto_20191122_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='geonodethemecustomization',
            name='footer_bg_color',
            field=models.CharField(default='#333333', max_length=10),
        ),
    ]