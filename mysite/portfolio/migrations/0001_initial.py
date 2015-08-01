# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('path', models.CharField(max_length=500)),
                ('meta_path', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
