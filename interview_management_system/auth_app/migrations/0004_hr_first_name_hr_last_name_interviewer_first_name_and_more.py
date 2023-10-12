# Generated by Django 4.2.6 on 2023-10-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_hr_department_alter_hr_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hr',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='hr',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='interviewer',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='interviewer',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]