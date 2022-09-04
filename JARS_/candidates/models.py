from django.db import models

# Create your models here.
class Candidate(models.Model):
  projects = models.PositiveIntegerField()
  skillmat = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  exp = models.FloatField()
  skills=models.TextField(max_length=50)
  projectss=models.TextField(max_length=50)
  status=models.CharField(max_length=50,default="Accepted")


