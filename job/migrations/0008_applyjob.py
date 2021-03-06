# Generated by Django 3.0.8 on 2020-07-19 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('apply_file', models.FileField(upload_to='apply_jobs/')),
                ('comment', models.TextField(max_length=1000)),
                ('job', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='job.Job')),
            ],
        ),
    ]
