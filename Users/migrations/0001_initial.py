# Generated by Django 4.1.3 on 2023-02-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bottlesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('bottleID', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'bottlesDB',
            },
        ),
    ]
