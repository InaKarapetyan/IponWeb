# Generated by Django 4.1.6 on 2023-02-24 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_customer_item_itemcategory_mybug_purchase_store_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="storecategory",
            name="pub_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
