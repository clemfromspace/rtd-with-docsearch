# Generated by Django 1.9.12 on 2017-10-09 20:14
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_build_command_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='cold_storage',
            field=models.NullBooleanField(help_text='Build steps stored outside the database.', verbose_name='Cold Storage'),
        ),
    ]
