# Generated by Django 5.0.1 on 2024-02-28 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0013_remove_students_bloodgroup_students_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]