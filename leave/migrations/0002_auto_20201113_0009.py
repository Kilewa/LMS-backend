# Generated by Django 3.1.3 on 2020-11-12 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='Comments',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='leave',
            old_name='Reasons',
            new_name='reasons',
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
