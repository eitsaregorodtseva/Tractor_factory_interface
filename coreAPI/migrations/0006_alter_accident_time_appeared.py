# Generated by Django 3.2.8 on 2021-10-22 02:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0005_alter_accident_time_appeared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='time_appeared',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 2, 26, 1, 473839, tzinfo=utc), verbose_name='Время создания инцидента'),
        ),
    ]
