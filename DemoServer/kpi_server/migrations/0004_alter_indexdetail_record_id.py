# Generated by Django 4.1 on 2023-09-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_server', '0003_alter_indexdetail_detail_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexdetail',
            name='record_id',
            field=models.CharField(blank=True, max_length=10, verbose_name='上传记录编号'),
        ),
    ]