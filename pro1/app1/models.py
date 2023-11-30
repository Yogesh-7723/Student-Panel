from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    
class Addcourse(models.Model):
    course = models.CharField(max_length=100)
    fees   = models.IntegerField()
    duration = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.course
    
class Addstudent(models.Model):
    sname =  models.CharField(max_length=100,null=True,blank=True)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=100)
    saddress = models.CharField(max_length=100)
    scollege = models.CharField(max_length=100)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    scourse = models.ForeignKey(Addcourse,on_delete=models.CASCADE)
    