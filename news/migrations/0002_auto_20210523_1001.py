# Generated by Django 2.2 on 2021-05-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]
