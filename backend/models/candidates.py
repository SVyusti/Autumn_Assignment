from django.db import models
from .ChoiceType import role_choices

class Candidates(models.Model):
    StudentId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    EnrollmentNo=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    EmailId=models.EmailField()
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250,choices=role_choices)
    year=models.CharField(max_length=250)
    RId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0,null=True)
    SId=models.ForeignKey('Season',on_delete=models.CASCADE,default=0,null=True)
    status=models.CharField(max_length=250,default="Registered")
    cg=models.FloatField()