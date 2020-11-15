# Generated by Django 3.1.3 on 2020-11-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'Employee'), (2, 'Dept_head'), (3, 'Admin')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='authentication.Role'),
        ),
    ]