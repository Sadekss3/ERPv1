# Generated by Django 4.1 on 2022-08-07 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERPapp', '0002_remove_project_postal_code_project_postal_code_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ERPapp.client'),
        ),
    ]
