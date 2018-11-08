# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-24 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_lianxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='班级名字')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('grade', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='app_lianxi.Grade', verbose_name='学生的班级')),
            ],
        ),
    ]