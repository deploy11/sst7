# Generated by Django 4.2.5 on 2023-09-11 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_sorov_ariza_mazmuni_alter_hokimiyat_muddat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hokimiyat',
            name='muddat',
            field=models.IntegerField(default=datetime.datetime(2023, 9, 12, 13, 27, 28, 183455, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='sorov',
            name='Yashashmanzili',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sorov',
            name='rasmvavidio',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
