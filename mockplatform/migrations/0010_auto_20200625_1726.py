# Generated by Django 3.0.7 on 2020-06-25 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mockplatform', '0009_auto_20200625_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_buyer_id', to='mockplatform.CardHolderDetails', to_field='uid'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_seller_id', to='mockplatform.CardHolderDetails', to_field='uid'),
        ),
    ]
