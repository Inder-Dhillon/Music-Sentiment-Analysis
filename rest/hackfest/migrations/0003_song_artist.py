# Generated by Django 2.1.4 on 2020-02-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackfest', '0002_auto_20200219_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
