# Generated by Django 4.1 on 2023-09-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_server', '0007_alter_userauth_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauth',
            name='is_superuser',
            field=models.BooleanField(default=False, verbose_name='是否超级用户'),
        ),
    ]
