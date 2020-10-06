# Generated by Django 2.2 on 2020-10-04 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0017_auto_20201004_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ni01',
            name='assayid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ni01s', to='assays.Assay'),
        ),
        migrations.AlterField(
            model_name='ni02rot01',
            name='assayid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ni02rot01s', to='assays.Assay'),
        ),
    ]
