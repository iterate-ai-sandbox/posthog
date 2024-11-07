# Generated by Django 4.2.15 on 2024-10-15 13:32

from django.db import migrations, models
from django.contrib.postgres.operations import AddConstraintNotValid, AddIndexConcurrently


class Migration(migrations.Migration):
    atomic = False  # Added to support concurrent index creation
    dependencies = [
        ("posthog", "0510_salesforce_missing_schemas"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""UPDATE posthog_grouptypemapping SET project_id = team_id;""",
            reverse_sql=migrations.RunSQL.noop,
            elidable=True,
        ),
        AddConstraintNotValid(
            model_name="grouptypemapping",
            constraint=models.CheckConstraint(
                name="group_type_project_id_is_not_null",
                check=models.Q(project_id__isnull=False),
            ),
        ),
        AddIndexConcurrently(
            model_name="grouptypemapping",
            index=models.Index(
                fields=("project", "group_type"),
                name="posthog_group_type_proj_idx",
            ),
        ),
        AddIndexConcurrently(
            model_name="grouptypemapping",
            index=models.Index(
                fields=("project", "group_type_index"),
                name="posthog_group_type_i_proj_idx",
            ),
        ),
    ]