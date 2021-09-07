# Generated by Django 3.2.6 on 2021-09-07 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Autores",
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
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("titulo", models.CharField(max_length=60)),
                ("descricao", models.TextField()),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]
