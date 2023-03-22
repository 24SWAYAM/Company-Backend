from django.db import models

# Create your models here
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    location  = models.CharField(max_length=50)
    about = models.TextField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100,choices = (('IT','IT'),('NON IT','NON IT'),("Mobile Phones",'Mobile Phones')))
    added_date = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    #Employees Model