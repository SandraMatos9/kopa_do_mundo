# Generated by Django 4.2.1 on 2023-05-31 19:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="title",
            new_name="titles",
        ),
    ]
