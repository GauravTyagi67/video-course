# Generated by Django 3.0.11 on 2021-02-06 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]