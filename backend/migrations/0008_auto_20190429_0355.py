# Generated by Django 2.2 on 2019-04-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_merge_20190429_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='employee_code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='employee_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='father_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='marital_status',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='mother_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='national_id',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='nationality',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='religion',
            field=models.CharField(max_length=30),
        ),
    ]
