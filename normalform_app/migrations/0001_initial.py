# Generated by Django 4.2.1 on 2023-06-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employe",
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
                ("role", models.CharField(max_length=50)),
                ("salary", models.CharField(max_length=50)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
