from django.db import models

class Candidates(models.Model):
    StudentId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=250)
    EnrollmentNo=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    EmailId=models.EmailField()
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    year=models.CharField(max_length=250)
    RId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
    SId=models.ForeignKey('Season',on_delete=models.CASCADE,default=0)
    status=models.CharField(max_length=250)
    cg=models.FloatField()