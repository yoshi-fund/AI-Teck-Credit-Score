# Generated by Django 4.2.5 on 2024-06-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("outstanding_debt", models.FloatField(verbose_name="債務（ドル建て）")),
                ("delay_from_due_date", models.FloatField(verbose_name="平均滞納日数")),
                ("num_of_delayed_payment", models.FloatField(verbose_name="平均滞納回数")),
                ("interest_rate", models.FloatField(verbose_name="クレカの利息")),
                ("num_bank_accounts", models.FloatField(verbose_name="保有口座数")),
                ("num_of_loan", models.FloatField(verbose_name="ローンの数")),
                ("num_credit_card", models.FloatField(verbose_name="クレカの保有枚数")),
                ("credit_score", models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
