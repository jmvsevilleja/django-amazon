# Generated by Django 3.0.3 on 2020-02-18 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date/Time'),
        ),
    ]
