# Generated by Django 2.1.3 on 2018-11-21 13:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_remove_page_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default=datetime.datetime(2018, 11, 21, 13, 19, 2, 403348, tzinfo=utc), max_length=100, verbose_name='Tytuł'),
            preserve_default=False,
        ),
    ]
