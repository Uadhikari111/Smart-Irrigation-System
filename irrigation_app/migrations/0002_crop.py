# Generated by Django 2.1.1 on 2019-01-26 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('irrigation_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irrigation_app.CropData')),
            ],
        ),
    ]