# Generated by Django 4.2.10 on 2024-03-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("phone", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("id_product", models.IntegerField()),
                ("id_user", models.IntegerField()),
                ("price", models.FloatField()),
                ("qty", models.IntegerField()),
                ("tax", models.FloatField()),
                ("total", models.FloatField()),
                ("discount", models.FloatField()),
                ("net", models.FloatField()),
                ("status", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
