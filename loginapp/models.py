from django.db import models

class users(models.Model):
    id= models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pwd=models.CharField(max_length=50)
    cpwd=models.CharField(max_length=50)


class employee_reg(models.Model):
    id= models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50,null=True,blank=True)
    lname=models.CharField(max_length=50,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    pwd=models.CharField(max_length=50,null=True,blank=True)
    cpwd=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=25,null=True,blank=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    department=models.CharField(max_length=50,null=True,blank=True)
    bloodgroup=models.CharField(max_length=50,null=True,blank=True)
    doj=models.DateField(null=True, blank=True)
    uploaddoc=models.FileField(upload_to='images/',null=True,blank=True)
    uploadpic=models.ImageField(upload_to='images/',null=True,blank=True)
    pnumber=models.IntegerField(null=True,blank=True)




