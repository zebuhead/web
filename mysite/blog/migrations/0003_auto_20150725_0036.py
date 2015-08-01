# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150725_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCitations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('work', models.CharField(max_length=200)),
                ('pages', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name=b'date')),
                ('link', models.CharField(default=b'No Link', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.CharField(default=b'All', max_length=200),
        ),
    ]
