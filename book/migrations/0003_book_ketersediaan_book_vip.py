# Generated by Django 4.2.6 on 2023-10-26 19:00

from django.db import migrations, models
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "data_buku.json")


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ketersediaan',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='vip',
            field=models.TextField(blank=True, null=True),
        ),
    ]
