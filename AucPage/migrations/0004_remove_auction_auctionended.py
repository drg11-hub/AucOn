# Generated by Django 3.1.7 on 2021-04-12 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AucPage', '0003_auction_auctionended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='AuctionEnded',
        ),
    ]