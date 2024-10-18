# Generated by Django 5.1.1 on 2024-10-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('student_phone_number', models.IntegerField()),
                ('student_email', models.EmailField(max_length=254)),
            ],
        ),
    ]