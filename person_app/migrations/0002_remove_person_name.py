# Generated by Django 4.1.5 on 2023-09-11 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
    ]