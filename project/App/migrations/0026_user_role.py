# Generated by Django 3.1.7 on 2021-07-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_auto_20210715_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Staff'), (3, 'Donors')], default=3),
        ),
    ]
