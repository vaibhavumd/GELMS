# Generated by Django 2.1.3 on 2018-12-01 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_tools'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tools',
        ),
    ]
