# Generated by Django 2.2.4 on 2019-08-16 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=12)),
                ('EmailId', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('DepartmentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='visitor.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('Salt', models.CharField(max_length=20)),
                ('isDeleted', models.BooleanField(default=False)),
                ('StartDate', models.DateTimeField()),
                ('ExpiredDate', models.DateTimeField()),
                ('Amount', models.DecimalField(decimal_places=4, max_digits=10000000)),
                ('EmailService', models.BooleanField(default=True)),
                ('CreatedDate', models.DateTimeField()),
                ('CreatedBy', models.CharField(max_length=50)),
                ('ModifiedBy', models.CharField(max_length=50)),
                ('ModifiedDate', models.DateTimeField()),
                ('Email', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('Pic', models.CharField(max_length=200)),
                ('IdType', models.CharField(max_length=50)),
                ('IdNumber', models.CharField(max_length=20)),
                ('IdPic', models.CharField(max_length=200)),
                ('InTime', models.TimeField()),
                ('OutTime', models.TimeField()),
                ('EmployeeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.Employee')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.UserRegistration')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.UserRegistration'),
        ),
        migrations.AddField(
            model_name='departments',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitor.UserRegistration'),
        ),
    ]
