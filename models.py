from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.username
    
class ContactModel(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    desc=models.TextField(max_length=150)
    
    def __str__(self):
        return self.name

class MeritModel(models.Model):
    sname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    caste=models.CharField(max_length=10)
    sphone=models.CharField(max_length=12)
    sclname=models.CharField(max_length=100)
    marks1=models.FileField()
    clgname=models.CharField(max_length=100)
    marks2=models.FileField()
    marks3=models.FileField()
    emrank=models.FileField()
    
    def __str__(self):
        return self.sname

class AthleticModel(models.Model):
    sname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    caste=models.CharField(max_length=3)
    sphone=models.CharField(max_length=12)
    sport=models.CharField(max_length=30)
    academy=models.CharField(max_length=100)
    authority=models.CharField(max_length=100)
    level=models.CharField(max_length=20)
    disabilities=models.CharField(max_length=12)
    
    def __str__(self):
        return self.sname
    
class EconomicalModel(models.Model):
    sname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    focc=models.CharField(max_length=100)
    mocc=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    caste=models.CharField(max_length=3)
    phone=models.CharField(max_length=12)
    sclname=models.CharField(max_length=100)
    clgname=models.CharField(max_length=100)
    income=models.FileField()
    
    def __str__(self):
        return self.sname
    
class Merit_Services(models.Model):
    service_name=models.CharField(max_length=122)
    service_amount=models.CharField(max_length=122)
    service_eligibility=models.CharField(max_length=122)
    
    def __str__(self):
        return self.service_name
    
class Sport_Services(models.Model):
    service1_name=models.CharField(max_length=122)
    service1_amount=models.CharField(max_length=122)
    service1_eligibility=models.CharField(max_length=122)
    
    def __str__(self):
        return self.service1_name

class Economical_Services(models.Model):
    service2_name=models.CharField(max_length=122)
    service2_amount=models.CharField(max_length=122)
    service2_eligibility=models.CharField(max_length=122)
    
    def __str__(self):
        return self.service2_name
