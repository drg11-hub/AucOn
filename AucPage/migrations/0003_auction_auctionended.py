# Generated by Django 3.1.7 on 2021-04-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AucPage', '0002_auto_20210410_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='AuctionEnded',
            field=models.CharField(default='No', max_length=3),
        ),
    ]