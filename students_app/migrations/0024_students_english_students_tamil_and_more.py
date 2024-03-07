# Generated by Django 5.0.1 on 2024-03-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0023_alter_students_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='english',
            field=models.BooleanField(default=False, verbose_name='English'),
        ),
        migrations.AddField(
            model_name='students',
            name='tamil',
            field=models.BooleanField(default=False, verbose_name='Tamil'),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=20, null=True),
        ),
    ]
