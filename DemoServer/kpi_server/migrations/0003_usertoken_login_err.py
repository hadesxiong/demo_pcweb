# Generated by Django 4.1 on 2023-09-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kpi_server", "0002_remove_userauth_last_login_remove_userauth_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertoken",
            name="login_err",
            field=models.IntegerField(default=0, help_text="登陆错误次数"),
        ),
    ]
