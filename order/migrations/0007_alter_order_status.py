# Generated by Django 3.2.7 on 2022-03-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
