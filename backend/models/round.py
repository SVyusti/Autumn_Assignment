
from django.db import models

class Round(models.Model):
    RoundId=models.IntegerField(primary_key=True)
    type=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    S_Id=models.ForeignKey('Season',on_delete=models.CASCADE,default=1)
