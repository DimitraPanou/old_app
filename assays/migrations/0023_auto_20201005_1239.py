# Generated by Django 2.2 on 2020-10-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0022_hem01_sample_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hem01',
            old_name='pdv',
            new_name='rdv',
        ),
    ]
