# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150725_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogimage',
            name='image',
            field=models.ImageField(default='exit', upload_to=b''),
            preserve_default=False,
        ),
    ]
