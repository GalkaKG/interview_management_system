# Generated by Django 4.2.6 on 2023-10-12 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('resume_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(choices=[('developer', 'Software Developer'), ('designer', 'Graphic Designer'), ('manager', 'Project Manager'), ('analyst', 'Business Analyst'), ('engineer', 'Mechanical Engineer')], max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('InProgress', 'In Progress'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Scheduled', max_length=20)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_management.candidate')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.interviewer')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackInterview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_management.candidate')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_management.interview')),
            ],
        ),
    ]
