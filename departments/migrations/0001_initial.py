# Generated by Django 3.1.3 on 2020-11-13 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('depart_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('employee_number', models.IntegerField(unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('designition', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('basic_pay', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('country_of_residence', models.CharField(max_length=100)),
                ('postal_address', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('depart_head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='departments.department')),
            ],
            options={
                'ordering': ('first_name',),
            },
        ),
    ]
