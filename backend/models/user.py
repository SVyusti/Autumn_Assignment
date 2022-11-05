from django.db import models
from .ChoiceType import role_choices
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings




class User(AbstractUser):
    role_choices=(("developer","Developer"),("designer","Designer"))
    UserId=models.AutoField(primary_key=True)
    username=models.CharField(max_length=300,unique=True)
    # password=models.CharField(max_length=300)
    name=models.CharField(max_length=300,null=True)
    EnrollmentNo=models.CharField(max_length=300,null=True)
    role=models.CharField(max_length=300,choices=role_choices,blank=True,null=True)
    branch=models.CharField(max_length=300,null=True)
    year=models.CharField(max_length=300,null=True)
    EmailId=models.EmailField()
    USERNAME_FIELD='UserId'
    REQUIRED_FIELDS=['email']
    phone=models.CharField(max_length=300,null=True)
    dob=models.DateField(null=True)

    def __str__(self):
        return self.username

