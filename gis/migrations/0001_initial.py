# Generated by Django 4.1.5 on 2023-01-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("brands", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("link_store", models.URLField()),
                ("price", models.IntegerField()),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "Low"), (1, "Mid"), (3, "High"), (4, "Commercial")]
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("Black", "Color Black"),
                            ("White", "Color White"),
                            ("Blue", "Color Blue"),
                            ("Bright", "Color Bright"),
                            ("Dark", "Color Dark"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gis",
                        to="brands.brand",
                    ),
                ),
            ],
        ),
    ]