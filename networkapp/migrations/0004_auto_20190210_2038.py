# Generated by Django 2.1.5 on 2019-02-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkapp', '0003_auto_20190210_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicecredentialdetail',
            name='device_ip',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
