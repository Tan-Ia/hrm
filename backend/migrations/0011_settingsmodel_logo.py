# Generated by Django 2.2 on 2019-04-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_settingsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsmodel',
            name='logo',
            field=models.ImageField(default='settings/hrm-logo.png', upload_to='settings/'),
        ),
    ]