# Generated by Django 3.2.7 on 2022-03-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 1), ('DONE', 2), ('CLOSE', 3)], default=1, max_length=50, null=True),
        ),
    ]
