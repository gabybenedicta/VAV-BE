# Generated by Django 3.0.7 on 2020-06-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockplatform', '0006_invoice_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller_id',
            field=models.CharField(max_length=100),
        ),
    ]
