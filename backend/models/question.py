from django.db import models


class Question(models.Model):
    QuestionId=models.AutoField(primary_key=True)
    problem=models.CharField(max_length=500)
    QuestionType=models.CharField(max_length=250)
    ModelAnswer=models.CharField(max_length=1000)
    TotalMarks=models.IntegerField()
    SeId=models.ForeignKey('Section',on_delete=models.CASCADE,default=0)