# Generated by Django 3.1.7 on 2021-07-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_user_nm'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fnm',
            field=models.CharField(max_length=50, null='True'),
            preserve_default='True',
        ),
    ]
