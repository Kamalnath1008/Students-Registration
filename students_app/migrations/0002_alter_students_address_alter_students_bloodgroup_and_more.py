# Generated by Django 5.0.1 on 2024-02-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Bloodgroup',
            field=models.CharField(blank=True, choices=[('o+ive', 'O+ive'), ('b+ive', 'B+ive'), ('a+ive', 'A+ive'), ('o-ive', 'O-ive'), ('a-ive', 'a-ive'), ('b-ive', 'b-ive'), ('ab+ive', 'AB+ive'), ('ab-ive', 'AB-ive'), ('other', 'OTHER')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Retypepass',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(blank=True, choices=[('select', 'select'), ('male', 'Male'), ('female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]