# Generated by Django 2.2 on 2021-05-01 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0013_fc07_pr02'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cba02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('dilution_factor', models.FloatField(blank=True, null=True)),
                ('igg1', models.FloatField(blank=True, null=True)),
                ('igg2a', models.FloatField(blank=True, null=True)),
                ('igg3', models.FloatField(blank=True, null=True)),
                ('iga', models.FloatField(blank=True, null=True)),
                ('igm', models.FloatField(blank=True, null=True)),
                ('igg2b', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cba02s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'managed': True,
                'db_table': 'CBA-02',
            },
        ),
        migrations.CreateModel(
            name='Cba01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('dilution_factor', models.FloatField(blank=True, null=True)),
                ('il_six', models.FloatField(blank=True, null=True)),
                ('il_ten', models.FloatField(blank=True, null=True)),
                ('il_twelve', models.FloatField(blank=True, null=True)),
                ('il_seventeen', models.FloatField(blank=True, null=True)),
                ('ifn_gamma', models.FloatField(blank=True, db_column='ifn-gamma', null=True)),
                ('tnf_alpha', models.FloatField(blank=True, db_column='tnf-alpha', null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cba01s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'managed': True,
                'db_table': 'CBA-01',
            },
        ),
    ]