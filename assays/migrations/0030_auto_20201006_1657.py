# Generated by Django 2.2 on 2020-10-06 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assays', '0029_biochem02'),
    ]

    operations = [
        migrations.AddField(
            model_name='biochem02',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Biochem03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timepoint', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('measurement_date', models.DateField(blank=True, null=True)),
                ('sample_source', models.CharField(blank=True, max_length=64, null=True)),
                ('alt', models.FloatField(blank=True, null=True)),
                ('ast', models.FloatField(blank=True, null=True)),
                ('alp', models.FloatField(blank=True, null=True)),
                ('total_bilirubin', models.FloatField(blank=True, null=True)),
                ('direct_bilirubin', models.FloatField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('assayid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biochem03s', to='assays.Assay')),
                ('mid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.CASCADE, to='assays.Mouse')),
            ],
            options={
                'managed': True,
                'db_table': 'BIOCHEM-03',
            },
        ),
    ]