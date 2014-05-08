from django.db import models

# Create your models here.

class Youth(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Bed_Gender = models.CharField(max_length=200)
    Phone_Number = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    Age_Verification = models.CharField(max_length=3)
    Notes = models.CharField(max_length=500)

    #Checkins
    First_Checkin = models.CharField(max_length=200)
    Last_Checkin = models.CharField(max_length=200)
    Rank = models.CharField(max_length=200)


    pub_date = models.DateTimeField('date published')