# Generated by Django 3.1.7 on 2021-07-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0023_auto_20210715_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='des',
        ),
        migrations.AddField(
            model_name='work',
            name='addres',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='work',
            name='age',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='email',
            field=models.EmailField(default=7, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='work',
            name='phno',
            field=models.CharField(max_length=30, null='True'),
            preserve_default='True',
        ),
    ]
