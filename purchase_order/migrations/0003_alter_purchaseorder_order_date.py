# Generated by Django 5.0.4 on 2024-05-09 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_order', '0002_alter_purchaseorder_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]