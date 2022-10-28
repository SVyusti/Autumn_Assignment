
from random import choice
from django.db import models
from .ChoiceType import role_choices

class Section(models.Model):
    # role_choices=(("developer","Developer"),("designer","Designer"))
    SectionId=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=50,choices=role_choices)
    max_marks=models.IntegerField()
    total_questions=models.IntegerField()
    RId=models.ForeignKey('Round',on_delete=models.CASCADE,default=0)
