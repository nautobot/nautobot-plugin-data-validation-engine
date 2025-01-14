# Generated by Django 3.2.21 on 2023-10-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_data_validation_engine", "0005_remove_slugs_alter_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datacompliance",
            name="message",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="datacompliance",
            name="validated_attribute",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="datacompliance",
            name="validated_attribute_value",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="datacompliance",
            name="validated_object_str",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="minmaxvalidationrule",
            name="error_message",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="regularexpressionvalidationrule",
            name="error_message",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="requiredvalidationrule",
            name="error_message",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="uniquevalidationrule",
            name="error_message",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]