# Generated by Django 5.0.1 on 2024-02-27 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0007_remove_students_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
    ]
