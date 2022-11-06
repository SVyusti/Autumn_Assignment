from django.db import models
from .ChoiceType import role_choices
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings




class User(AbstractUser):
    role_choices=(("developer","Developer"),("designer","Designer"))
    UserId=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=300,unique=True,blank=True)
    # password=models.CharField(max_length=300)
    name=models.CharField(max_length=300,null=True,blank=True)
    EnrollmentNo=models.CharField(max_length=300,null=True,blank=True)
    role=models.CharField(max_length=300,choices=role_choices,blank=True,null=True)
    branch=models.CharField(max_length=300,null=True,blank=True)
    year=models.CharField(max_length=300,null=True,blank=True)
    EmailId=models.CharField(max_length=200,blank=True)
    USERNAME_FIELD='UserId'
    REQUIRED_FIELDS=['email','username']
    phone=models.CharField(max_length=300,null=True,blank=True)
    dob=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.username

