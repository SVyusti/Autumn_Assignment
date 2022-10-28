
from django.db import models
from .ChoiceType import role_choices

class Round(models.Model):
    RoundId=models.IntegerField(primary_key=True)
    type=models.CharField(max_length=100)
    role=models.CharField(max_length=50,choices=role_choices)
    S_Id=models.ForeignKey('Season',on_delete=models.CASCADE,default=1)
