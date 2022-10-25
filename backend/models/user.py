from django.db import models

class User(models.Model):
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    name=models.CharField(max_length=300)
    EnrollmentNo=models.CharField(max_length=300)
    role=models.CharField(max_length=300)
    branch=models.CharField(max_length=300)
    year=models.CharField(max_length=300)
    EmailId=models.EmailField()
    phone=models.CharField(max_length=300)
    dob=models.DateField()