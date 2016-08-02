# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='msg_code',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'Message Unique Code', db_index=True),
        ),
    ]
