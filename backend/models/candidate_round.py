from django.db import models
from .ChoiceType import evaluation_choices

class Candidate_round(models.Model):
    RoundId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
    candidateId=models.ForeignKey('Candidates',on_delete=models.CASCADE,default=0)
    TimeSlot=models.CharField(max_length=250)
    EvaluationStatus=models.CharField(max_length=250,choices=evaluation_choices)
    RoundStatus=models.CharField(max_length=250)