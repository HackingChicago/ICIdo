# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 03:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='amount_raised',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Donor'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.Portfolio'),
        ),
    ]
