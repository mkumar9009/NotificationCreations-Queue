# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('notifications_type', models.SmallIntegerField(default=0, max_length=10, choices=[(0, 'Admin'), (1, 'Individual')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deliver_time', models.DateTimeField()),
                ('content', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email_address', models.EmailField(max_length=80, unique=True)),
                ('phoneno', models.CharField(max_length=15, validators=[django.core.validators.MaxLengthValidator(14), django.core.validators.MinLengthValidator(10), django.core.validators.validate_integer])),
                ('user_img', models.ImageField(null=True, upload_to='image/user/', blank=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('lastvisit_date', models.DateTimeField()),
                ('address', models.CharField(null=True, max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(to='testapp.UserType'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='user_type',
            field=models.ForeignKey(to='testapp.UserType'),
        ),
    ]
