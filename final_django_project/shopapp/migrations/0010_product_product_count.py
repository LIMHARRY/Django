# Generated by Django 2.1.4 on 2019-01-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_auto_20190104_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
