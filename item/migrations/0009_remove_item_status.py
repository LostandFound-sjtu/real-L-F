# Generated by Django 2.1.5 on 2020-05-29 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20200525_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
    ]
