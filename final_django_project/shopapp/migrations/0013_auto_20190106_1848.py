# Generated by Django 2.1.4 on 2019-01-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0012_product_big_product_middle_product_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_middle',
            name='aisle_id',
            field=models.IntegerField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
