# Generated by Django 3.2.9 on 2021-12-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_roommodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='room_Img1',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='room_Img2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='room_Img3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]