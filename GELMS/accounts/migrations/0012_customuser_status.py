# Generated by Django 2.1 on 2018-11-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20181115_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher')], default='STUDENT', max_length=10),
        ),
    ]