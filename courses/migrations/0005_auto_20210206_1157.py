# Generated by Django 3.0.11 on 2021-02-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20210206_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Video_id',
            field=models.CharField(max_length=100),
        ),
    ]
