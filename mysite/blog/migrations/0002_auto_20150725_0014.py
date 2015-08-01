# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.CharField(default='exit', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogimage',
            name='blog',
            field=models.ForeignKey(to='blog.Blog'),
        ),
    ]
