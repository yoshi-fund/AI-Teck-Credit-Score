# Generated by Django 4.2.5 on 2024-06-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="cluster",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "安定型(財務基盤強し)"),
                    (1, "負債と建物を大量に所持"),
                    (2, "The 平均"),
                    (3, "出来杉くん(優秀)"),
                ],
                null=True,
                verbose_name="クラスター",
            ),
        ),
    ]
