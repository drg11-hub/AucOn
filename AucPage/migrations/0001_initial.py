# Generated by Django 3.1.7 on 2021-04-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OwnerID', models.IntegerField()),
                ('ProductID', models.IntegerField()),
                ('ClientUsername', models.CharField(max_length=30)),
                ('ClientID', models.IntegerField()),
                ('ClientInitialBid', models.IntegerField()),
                ('Winner', models.CharField(default='No', max_length=3)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
