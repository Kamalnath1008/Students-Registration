# Generated by Django 5.0.1 on 2024-02-27 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0004_alter_students_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='students',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='students',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='students',
            name='Retypepass',
        ),
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='students',
            name='phonenumber',
        ),
    ]
