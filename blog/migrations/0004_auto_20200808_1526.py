# Generated by Django 2.2.15 on 2020-08-08 21:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_nominations_published_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nominations',
            new_name='Nomination',
        ),
    ]