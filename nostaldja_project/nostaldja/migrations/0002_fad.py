# Generated by Django 4.1.7 on 2023-03-29 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("nostaldja", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fad",
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
                ("name", models.CharField(max_length=100)),
                ("image_url", models.TextField()),
                ("description", models.CharField(max_length=200)),
                (
                    "decade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fads",
                        to="nostaldja.decade",
                    ),
                ),
            ],
        ),
    ]
