# Generated by Django 2.2 on 2020-09-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0003_auto_20200901_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iinflc04',
            name='timepoint_type',
        ),
        migrations.AddField(
            model_name='iinflc04',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]