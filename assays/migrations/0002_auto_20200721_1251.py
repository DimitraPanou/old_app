# Generated by Django 2.2 on 2020-07-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mouse',
            name='mouse_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='mid',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
