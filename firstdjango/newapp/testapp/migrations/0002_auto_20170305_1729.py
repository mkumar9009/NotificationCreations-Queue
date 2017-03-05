# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name_plural': 'User Type'},
        ),
        migrations.AlterField(
            model_name='notifications',
            name='notifications_type',
            field=models.SmallIntegerField(default=0, choices=[(0, 'Admin'), (1, 'Individual')]),
        ),
    ]
