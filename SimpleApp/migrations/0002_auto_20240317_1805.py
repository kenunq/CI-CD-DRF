# Generated by Django 5.0.3 on 2024-03-17 18:05

from django.db import migrations


def add_sample_data(apps, schema_editor):
    SimpleModel = apps.get_model("SimpleApp", "SimpleModel")
    SimpleModel.objects.create(SimpleText="Text 1")
    SimpleModel.objects.create(SimpleText="Text 2")
    SimpleModel.objects.create(SimpleText="Text 3")


class Migration(migrations.Migration):
    dependencies: list[tuple[str, str]] = [
        ("SimpleApp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_sample_data),
    ]
