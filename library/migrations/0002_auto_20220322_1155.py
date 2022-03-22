# Generated by Django 3.2 on 2022-03-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=10)),
                ("email", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="library.Author"),
        ),
    ]