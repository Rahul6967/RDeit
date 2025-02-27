# Generated by Django 4.2.10 on 2024-06-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Template",
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
                ("TempName", models.CharField(max_length=30)),
                ("Description", models.CharField(max_length=100)),
                ("thumbnail", models.ImageField(upload_to="images")),
                ("template", models.FileField(upload_to="documents")),
            ],
        ),
    ]
