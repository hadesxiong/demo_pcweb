# Generated by Django 4.1 on 2023-09-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_server', '0002_alter_indexdetail_record_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexdetail',
            name='detail_value',
            field=models.IntegerField(blank=True, verbose_name='指标具体值'),
        ),
    ]