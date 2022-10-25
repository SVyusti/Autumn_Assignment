from django.db import models

class Candidate_score(models.Model):
    studentId=models.ForeignKey('Candidates',on_delete=models.CASCADE,default=0)
    QuestionId=models.ForeignKey('Question',on_delete=models.CASCADE,default=0)
    marks_obtained=models.IntegerField()
    AnswerGiven=models.CharField(max_length=500)
    remarks=models.CharField(max_length=500)