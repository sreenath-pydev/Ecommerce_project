# Generated by Django 5.0.1 on 2024-04-03 18:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customers_user'),
        ('orders', '0003_alter_order_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderd_item', to='customer.customers'),
        ),
    ]
