from django.db import models

# Create your models here.
class Template(models.Model):
    TempName=models.CharField(max_length=30)
    Description=models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='thumbnail/')
    template=models.FileField(upload_to='tempfile/')

class Userdetailmodel(models.Model):
    fullname=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    profile=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    dateofbirth=models.DateField()
    user_type_choices = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    ]
    gender = models.CharField(max_length=20,choices=user_type_choices,default='male')
    phoneno=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    skill1=models.CharField(max_length=20)
    skill2=models.CharField(max_length=20)
    skill3=models.CharField(max_length=20)
    skill4=models.CharField(max_length=20)
    skill5=models.CharField(max_length=20)
    skill6=models.CharField(max_length=20)
    education1=models.CharField(max_length=50)
    education2=models.CharField(max_length=50)
    education3=models.CharField(max_length=50)
    institute1=models.CharField(max_length=100)
    institute2=models.CharField(max_length=100)
    institute3=models.CharField(max_length=100)
    experience1=models.CharField(max_length=100)
    experience2=models.CharField(max_length=100)
    description1=models.CharField(max_length=100)
    description2=models.CharField(max_length=100)
