from django.db import models

class Season(models.Model):
    Id=models.IntegerField(primary_key=True)
    year=models.CharField(max_length=50)
    class Meta(object):
        app_label = 'backend'
