# Generated by Django 4.2.10 on 2024-03-10 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Furniture",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="FurnitureDetails",
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
                ("color", models.CharField(max_length=50)),
                ("price", models.FloatField()),
                ("qty", models.IntegerField()),
                ("tax", models.FloatField()),
                ("image", models.CharField(max_length=150, null=True)),
                ("total", models.FloatField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "itemsid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="furniture.furniture",
                    ),
                ),
            ],
        ),
    ]
