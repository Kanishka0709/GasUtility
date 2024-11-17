# Generated by Django 5.1.3 on 2024-11-17 13:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(max_length=12, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('request_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('resolution_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
            ],
        ),
    ]
