# Generated by Django 3.1.7 on 2021-07-15 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_auto_20210715_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='work',
            name='last_name',
        ),
    ]
