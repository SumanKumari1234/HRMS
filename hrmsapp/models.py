from django.db import models


class user(models.Model):
    eid = models.CharField(max_length=100)
    efirstname = models.CharField(max_length=100)
    elastname = models.CharField(max_length=100,null=True,blank=True)
    edepartment = models.CharField(max_length=50,null=True,blank=True)
    edesignation = models.CharField(max_length=50,null=True,blank=True)
    leavetype= models.CharField(max_length=100)
    econtact = models.BigIntegerField(null=True,blank=True)
    noofdays = models.IntegerField(null=True,blank=True)
    fromdate = models.DateField(null=True, blank=True)
    todate = models.DateField(null=True,blank=True)
    submitteddate = models.DateField(null=True,blank=True)
    uploadfile = models.FileField(upload_to='images/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    class Meta:
        db_table = "user"



class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"


class Department(models.Model):
    department_code = models.CharField(max_length=20)
    department_name = models.CharField(max_length=100)
    department_head = models.CharField(max_length=100)
    department_description = models.TextField()

    class Meta:
        db_table = "Department"


class Designation(models.Model): 
    designation_title = models.CharField(max_length=20) 
    designation_code = models.CharField(max_length=100) 
    designation_head = models.CharField(max_length=100) 
    designation_description = models.TextField() 
 
    class Meta: 
        db_table = "Designation"


class Disciplinary(models.Model): 
    employee_name = models.CharField(max_length=100) 
    employee_code = models.IntegerField (unique=True) 
    disciplinary_action = models.TextField() 
    date_of_action = models.DateField() 
    disciplinary_notes = models.TextField() 
 
    class Meta: 
        db_table = "disciplinary"