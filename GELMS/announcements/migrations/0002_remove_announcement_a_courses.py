# Generated by Django 2.1 on 2018-11-17 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='a_courses',
        ),
    ]