# Generated by Django 4.1 on 2023-09-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_server', '0004_rename_record_id_indexdetail_detail_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexdetail',
            name='detail_id',
            field=models.CharField(blank=True, help_text='上传记录编号', max_length=48),
        ),
    ]