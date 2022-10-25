from django.db import models

class Evaluator(models.Model):
    EvaluatorId=models.IntegerField(primary_key=True)
    UserId=models.ForeignKey('User',on_delete=models.CASCADE,default=0)
    SId=models.ForeignKey('Season',on_delete=models.CASCADE,default=0)
    PanelId=models.IntegerField()
    name=models.CharField(max_length=300)