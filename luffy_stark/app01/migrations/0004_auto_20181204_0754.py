# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-04 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deploy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('status', models.IntegerField(choices=[(1, '在线'), (2, '离线')], verbose_name='状态')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='classes',
            field=models.IntegerField(choices=[(11, '全栈1期'), (21, '全栈3期')], default=11, verbose_name='班级'),
        ),
    ]
