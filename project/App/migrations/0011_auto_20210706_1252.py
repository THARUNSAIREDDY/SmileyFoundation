# Generated by Django 3.1.7 on 2021-07-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20210706_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='fathername',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='fatheroccupation',
            field=models.CharField(max_length=25),
        ),
    ]