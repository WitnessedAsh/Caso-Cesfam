# Generated by Django 3.2.3 on 2022-05-19 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CesfamApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescripcion',
            old_name='medico',
            new_name='Username',
        ),
    ]
