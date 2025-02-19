# Generated by Django 5.0.6 on 2024-06-07 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.IntegerField(max_length=100)),
                ('case_status', models.CharField(max_length=100)),
                ('case_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('govt_id', models.IntegerField(max_length=100)),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.case')),
            ],
        ),
    ]
