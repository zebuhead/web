# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]
