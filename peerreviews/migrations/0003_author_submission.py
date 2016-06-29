# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peerreviews', '0002_auto_20160624_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default=None, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('venue', models.TextField(null=True)),
                ('status', models.CharField(max_length=100)),
                ('reviewdeadline', models.DateField(default=None)),
                ('link', models.URLField(null=True)),
                ('attachment', models.FileField(null=True, upload_to=b'')),
                ('authors', models.ManyToManyField(to='peerreviews.Author')),
                ('reviewers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerreviews.Reviewer')),
            ],
        ),
    ]