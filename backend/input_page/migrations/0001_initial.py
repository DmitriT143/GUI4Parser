# Generated by Django 5.0.6 on 2024-07-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('link', models.CharField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=36)),
                ('workday', models.CharField(max_length=20)),
                ('tags', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('link', models.CharField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=15)),
                ('salary_min', models.CharField(max_length=18)),
                ('salary_max', models.CharField(max_length=18)),
                ('workday', models.CharField(max_length=20)),
                ('requirements', models.CharField()),
                ('responsibilities', models.CharField()),
            ],
        ),
    ]
