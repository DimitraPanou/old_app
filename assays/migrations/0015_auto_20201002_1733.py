# Generated by Django 2.2 on 2020-10-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0014_auto_20200929_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atype',
            name='assay_word',
            field=models.FileField(blank=True, upload_to='assays/types/<django.db.models.fields.CharField>/'),
        ),
    ]
