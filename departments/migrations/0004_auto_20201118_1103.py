# Generated by Django 3.1.3 on 2020-11-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0003_auto_20201118_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
