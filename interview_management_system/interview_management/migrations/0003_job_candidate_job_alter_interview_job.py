# Generated by Django 4.2.6 on 2023-10-15 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview_management', '0002_alter_interview_date_alter_interview_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('developer', 'Software Developer'), ('designer', 'Graphic Designer'), ('manager', 'Project Manager'), ('analyst', 'Business Analyst'), ('engineer', 'Mechanical Engineer')], max_length=100)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interview_management.job'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='interview_management.job'),
        ),
    ]
