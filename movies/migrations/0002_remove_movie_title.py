# Generated by Django 4.2 on 2024-02-23 14:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="title",
        ),
    ]
