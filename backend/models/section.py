
from django.db import models

class Section(models.Model):
    SectionId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=50)
    max_marks=models.IntegerField()
    total_questions=models.IntegerField()
    RId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
