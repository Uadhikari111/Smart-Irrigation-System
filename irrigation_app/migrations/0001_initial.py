# Generated by Django 2.1.1 on 2019-01-26 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropData',
            fields=[
                ('crop_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('moisture_value', models.IntegerField()),
            ],
        ),
    ]
