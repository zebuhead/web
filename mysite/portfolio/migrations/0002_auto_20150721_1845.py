# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('authors', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Maps',
        ),
        migrations.AddField(
            model_name='map',
            name='project',
            field=models.ForeignKey(to='portfolio.Project'),
        ),
    ]
