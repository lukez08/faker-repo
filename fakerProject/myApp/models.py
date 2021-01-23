from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=40)
    roll=models.IntegerField()
    marks=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    