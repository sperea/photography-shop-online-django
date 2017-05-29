# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170529_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsize',
            options={'ordering': ('name',), 'verbose_name': 'productsize', 'verbose_name_plural': 'productsizes'},
        ),
    ]
