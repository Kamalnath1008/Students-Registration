# Generated by Django 5.0.1 on 2024-02-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0016_remove_students_address_remove_students_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]