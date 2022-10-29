from django.db import models
from .ChoiceType import role_choices
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    role_choices=(("developer","Developer"),("designer","Designer"))
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=300,unique=True)
    password=models.CharField(max_length=300)
    name=models.CharField(max_length=300)
    EnrollmentNo=models.CharField(max_length=300)
    role=models.CharField(max_length=300,choices=role_choices)
    branch=models.CharField(max_length=300)
    year=models.CharField(max_length=300)
    EmailId=models.EmailField()
    USERNAME_FIELD='username'
    phone=models.CharField(max_length=300)
    dob=models.DateField()

