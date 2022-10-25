from django.db import models

class Candidate_round(models.Model):
    RoundId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
    candidateId=models.ForeignKey('Candidates',on_delete=models.CASCADE,default=0)
    TimeSlot=models.CharField(max_length=250)
    EvaluationStatus=models.CharField(max_length=250)
    RoundStatus=models.CharField(max_length=250)