# Generated by Django 2.2 on 2020-10-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0015_auto_20201002_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='atype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
