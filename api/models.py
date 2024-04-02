from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50)
    companyLocation = models.CharField(max_length=100)
    companyAbout = models.TextField(max_length=100)
    companyType = models.CharField(max_length=100, choices=(('IT', 'IT'),('Non IT', 'Non IT')))
    companyActive = models.BooleanField(default=False)