from django.db import models

# Create your models here.
class Jobs(models.Model):
    JobID=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=50)
    Skills=models.CharField(max_length=50)
    Description=models.TextField(max_length=1000)
