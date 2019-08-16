# Generated by Django 2.1.2 on 2019-08-16 20:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('visitor', '0003_auto_20190817_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='Amount',
            field=models.DecimalField(decimal_places=4, max_digits=10000000, null=True),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='CreatedBy',
            field=models.CharField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 278617, tzinfo=utc), max_length=50),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='CreatedDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 277616, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='Email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='EmailService',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='ExpiredDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 277616, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='MobileNo',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='ModifiedBy',
            field=models.CharField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 278617, tzinfo=utc), max_length=50),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='ModifiedDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 278617, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='Salt',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='StartDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 20, 7, 6, 277616, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='isDeleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
