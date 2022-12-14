# Generated by Django 4.1 on 2022-08-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERPapp', '0012_invoice_payment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'paid'), ('not paid', 'not_paid')], default='not paid', max_length=20),
        ),
    ]
