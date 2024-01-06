from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StudentResultSheet(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    roll = models.IntegerField(null=True,blank=True)
    
    
    exam_sheet = models.ImageField(upload_to="student/",null=True,blank=True)
    physics = models.IntegerField(null=True,blank=True)
    chemistry = models.IntegerField(null=True,blank=True)
    math = models.IntegerField(null=True,blank=True)
    english = models.IntegerField(null=True,blank=True)
    analytical = models.IntegerField(null=True,blank=True)
    result = models.IntegerField(null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.name}-{self.dept}-{self.batch}-{self.subject}"

class AnswerSheet(models.Model):
    subject = models.CharField(max_length=50,null=True,blank=True)
    dept = models.CharField(max_length=50,null=True,blank=True)
    batch = models.IntegerField(null=True,blank=True)
    examiner = models.CharField(max_length=50,null=True,blank=True)
    code = models.CharField(max_length=10,null=True,blank=True)
    students = models.ManyToManyField(StudentResultSheet,blank=True)
    result_sheet = models.ImageField(upload_to="result/",null=True,blank=True)
    
    def __str__(self) -> str:
        return f"{self.dept}-{self.batch} {self.subject}"
    
    
