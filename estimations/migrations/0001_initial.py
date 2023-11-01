# Generated by Django 4.2.5 on 2023-11-01 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("total_amps", models.PositiveIntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ControlFlow",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.TextField(blank=True, null=True)),
                ("digital_input_num", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("digital_input_str", models.CharField(blank=True, max_length=255, null=True)),
                ("digital_output_num", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("digital_output_str", models.CharField(blank=True, max_length=255, null=True)),
                ("analog_input_num", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("analog_input_str", models.CharField(blank=True, max_length=255, null=True)),
                ("analog_output_num", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("analog_output_str", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ExtraItems",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveSmallIntegerField()),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("quote_number", models.PositiveIntegerField(blank=True, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("slug", models.CharField(max_length=255)),
                ("item_type", models.CharField(max_length=255)),
                (
                    "voltage_supply",
                    models.IntegerField(
                        choices=[(0, "unknown"), (1, "240v/P1"), (2, "415v/3P"), (3, "24DC"), (4, "24AC")], default=0
                    ),
                ),
                (
                    "power",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Power (kW)"
                    ),
                ),
                (
                    "current",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="I (A)"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "board",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="estimations.board",
                    ),
                ),
                (
                    "control_flow",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="items",
                        to="estimations.controlflow",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="estimations.project",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="controlflow",
            name="extra_items",
            field=models.ManyToManyField(blank=True, related_name="control_flow", to="estimations.extraitems"),
        ),
        migrations.AddField(
            model_name="controlflow",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="control_flow", to="estimations.board"
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="boards", to="estimations.project"
            ),
        ),
    ]