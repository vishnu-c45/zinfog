from django.db import models

# Create your models here.

class Student_Registration(models.Model):
    name=models.CharField(max_length=100,null=True)
    date_of_birth=models.DateField()
    username=models.CharField(max_length=100,null=True)
    profile_pic=models.FileField(upload_to='images/', null=True, blank=True)
    phonenumber=models.IntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,default="")
    email=models.CharField(max_length=100,default="")
    bio=models.CharField(max_length=100,default="")
    
class Admin_Registration(models.Model):    
    name=models.CharField(max_length=100,null=True)
    date_of_birth=models.DateField()
    profile_pic=models.ImageField(upload_to='images/', null=True, blank=True)
    username=models.CharField(max_length=100,null=True)
    phonenumber=models.IntegerField(null=True)
    password=models.CharField(max_length=100,null=True)
    
    
class Student_Mark(models.Model):
    student=models.ForeignKey(Student_Registration,on_delete=models.CASCADE)  
    maths_marks=models.CharField(max_length=100,default='')
    physics_marks=models.CharField(max_length=100,default='')
    chemistry_marks=models.CharField(max_length=100,default='')