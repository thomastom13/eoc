# Generated by Django 4.0.2 on 2022-04-17 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryblog', '0012_post_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
