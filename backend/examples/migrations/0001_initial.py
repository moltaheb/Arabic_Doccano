# Generated by Django 3.2.11 on 2022-01-28 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0034_auto_20220128_0246"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Example",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                            ),
                        ),
                        ("uuid", models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                        ("meta", models.JSONField(default=dict)),
                        ("filename", models.FileField(default=".", max_length=1024, upload_to="")),
                        ("text", models.TextField(blank=True, null=True)),
                        ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                        ("updated_at", models.DateTimeField(auto_now=True)),
                        (
                            "annotations_approved_by",
                            models.ForeignKey(
                                blank=True,
                                null=True,
                                on_delete=django.db.models.deletion.SET_NULL,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                        (
                            "project",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE, related_name="examples", to="api.project"
                            ),
                        ),
                    ],
                    options={
                        "ordering": ["created_at"],
                    },
                ),
                migrations.CreateModel(
                    name="Comment",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                            ),
                        ),
                        ("text", models.TextField()),
                        ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                        ("updated_at", models.DateTimeField(auto_now=True)),
                        (
                            "example",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="comments",
                                to="examples.example",
                            ),
                        ),
                        (
                            "user",
                            models.ForeignKey(
                                null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                            ),
                        ),
                    ],
                    options={
                        "ordering": ["created_at"],
                    },
                ),
                migrations.CreateModel(
                    name="ExampleState",
                    fields=[
                        (
                            "id",
                            models.BigAutoField(
                                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                            ),
                        ),
                        ("confirmed_at", models.DateTimeField(auto_now=True)),
                        (
                            "confirmed_by",
                            models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                        ),
                        (
                            "example",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                related_name="states",
                                to="examples.example",
                            ),
                        ),
                    ],
                    options={
                        "unique_together": {("example", "confirmed_by")},
                    },
                ),
            ]
        )
    ]
