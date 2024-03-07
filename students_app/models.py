from django.db import models
# from django import forms

# Create your models here.
class Students(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    Retypepass=models.CharField(max_length=20,null=True,blank=True)
    Phnumber=models.IntegerField(blank=True,null=True)
    Address=models.CharField(max_length=200,null=True,blank=True)
    Age=models.IntegerField(blank=True,null=True)
    bgroup=[('o+ive','O+ive'),('b+ive','B+ive'),('a+ive','A+ive'),('o-ive','O-ive'),('a-ive','a-ive'),('b-ive','b-ive'),('ab+ive','AB+ive'),('ab-ive','AB-ive'),('other','OTHER')]
    Bloodgroup=models.CharField(choices=bgroup,max_length=20,null=True,blank=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    gen=[('male','Male'),('female','Female')]
    gender=models.CharField(choices=gen,max_length=20,null=True,blank=True)
    tamil=models.BooleanField("Tamil",default=False)
    english=models.BooleanField("English",default=False)
    def __str__(self):
        return self.gender
    def __str__(self):
        return self.Bloodgroup
    class Meta:
        db_table="jaga"
    
    
