# Generated by Django 4.0.5 on 2023-03-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_shippingaddress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
