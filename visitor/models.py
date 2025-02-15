from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.hashers import make_password
# Create your models here.
class UserRegistration(models.Model):
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=100, null=True)
    ConfirmPassword = models.CharField(max_length=100, null=True)
    Name = models.CharField(max_length=50, null=True)
    Salt = models.CharField(max_length=20, null=True)
    isDeleted = models.BooleanField(null=True, default=False)
    StartDate = models.DateTimeField(null=False,default=datetime.now)
    ExpiredDate = models.DateTimeField(null=False,default=datetime.now)
    Amount = models.DecimalField(null=True, max_digits=10000000, decimal_places=4)
    EmailService = models.BooleanField(null=True, default=True)
    CreatedDate = models.DateTimeField(default=datetime.now)
    CreatedBy = models.CharField(max_length=50,default="admin")
    ModifiedBy = models.CharField(max_length=50,default="admin")
    ModifiedDate = models.DateTimeField(default=datetime.now)
    Email = models.CharField(max_length=100,default="")
    MobileNo = models.CharField(max_length=12,default="")

    def save(self, *args, **kwargs):
        self.Password = make_password(self.Password)
        self.ConfirmPassword = make_password(self.ConfirmPassword)
        super(UserRegistration, self).save(*args, **kwargs)


class Departments(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=False)
    DepartmentName = models.CharField(max_length=100)


class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=False)
    DepartmentId = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    MobileNo = models.CharField(max_length=12, null=False)
    EmailId = models.CharField(max_length=100, null=False)
    Address = models.CharField(max_length=200)


class Visitors(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100, null=False)
    MobileNo = models.CharField(max_length=12, null=False)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    Pic = models.CharField(max_length=200)
    IdType = models.CharField(max_length=50)
    IdNumber = models.CharField(max_length=20)
    IdPic = models.CharField(max_length=200)
    InTime = models.TimeField()
    OutTime = models.TimeField()