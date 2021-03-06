# Generated by Django 2.2.15 on 2020-08-09 13:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contracts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomination',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Contracts'),
        ),
        migrations.AlterField(
            model_name='nomination',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 13, 35, 38, 57713, tzinfo=utc), null=True),
        ),
    ]
