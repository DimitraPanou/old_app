# Generated by Django 2.2 on 2020-09-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0002_auto_20200721_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atype',
            name='assay_word',
            field=models.FileField(upload_to='assays/types/<django.db.models.fields.CharField>/'),
        ),
    ]
