# Generated by Django 4.1 on 2023-09-06 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi_server', '0006_userauth'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userauth',
            table='user_auth',
        ),
    ]
