# Generated by Django 4.2.6 on 2023-10-15 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
