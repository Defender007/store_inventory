# Generated by Django 5.0.6 on 2024-06-22 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=155)),
            ],
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="contact_info",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact",
                to="inventory.contact",
            ),
        ),
    ]
