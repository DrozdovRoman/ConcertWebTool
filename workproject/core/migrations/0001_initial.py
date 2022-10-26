# Generated by Django 4.1.2 on 2022-10-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Concert",
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
                (
                    "name",
                    models.CharField(max_length=30, verbose_name="Название Концерта"),
                ),
                ("city", models.CharField(max_length=30, verbose_name="Город")),
                ("concert_date", models.DateField(verbose_name="Дата")),
                (
                    "status",
                    models.CharField(max_length=10, verbose_name="Статус Концерта"),
                ),
            ],
        ),
    ]