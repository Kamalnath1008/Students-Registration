# Generated by Django 5.0.1 on 2024-02-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0020_remove_students_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Phnumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
