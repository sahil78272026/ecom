# Generated by Django 4.0.5 on 2023-03-23 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
