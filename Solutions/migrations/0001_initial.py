# Generated by Django 4.2.11 on 2024-06-25 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=15, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
