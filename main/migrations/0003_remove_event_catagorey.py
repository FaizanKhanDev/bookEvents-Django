# Generated by Django 4.2.1 on 2023-05-28 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_event_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='catagorey',
        ),
    ]