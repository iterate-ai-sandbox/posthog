# Generated by Django 4.2.15 on 2024-11-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0522_datawarehouse_salesforce_opportunity"),
    ]

    operations = [
        migrations.AddField(
            model_name="errortrackingsymbolset",
            name="content_hash",
            field=models.TextField(null=True),
        ),
    ]