# Generated by Django 4.1 on 2022-08-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERPapp', '0014_alter_invoice_payment_status_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='type_of_document',
            field=models.CharField(choices=[('Sales Receipt', 'Receipt Sales'), ('Retail Sales Invoice', 'Retail Sales Invoice'), ('VAT Sales Invoice', 'VAT Sales Invoice'), ('Purchase Receipt', 'Receipt Purchase'), ('Retail Purchase Invoice', 'Retail Purchase Invoice'), ('VAT Purchase Invoice', 'VAT Purchase Invoice')], default='VAT Purchase Invoice', max_length=30),
        ),
    ]
