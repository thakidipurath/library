# Generated by Django 4.0.1 on 2022-02-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]