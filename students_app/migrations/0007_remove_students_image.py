# Generated by Django 5.0.1 on 2024-02-27 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0006_students_address_students_age_students_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]