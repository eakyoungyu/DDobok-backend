# Generated by Django 4.1.5 on 2023-01-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gis", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gi",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="gi",
            name="priority",
            field=models.IntegerField(
                choices=[(0, "Low"), (1, "Mid"), (3, "High"), (4, "Commercial")],
                default=0,
            ),
        ),
    ]
