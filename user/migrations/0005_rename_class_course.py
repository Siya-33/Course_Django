# Generated by Django 4.0.4 on 2022-06-21 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_class'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Course',
        ),
    ]
