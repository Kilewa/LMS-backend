# Generated by Django 3.1.3 on 2020-11-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201118_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmenthead',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
