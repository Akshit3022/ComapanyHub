from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=50)
    companyLocation = models.CharField(max_length=100)
    companyAbout = models.TextField(max_length=100)
    companyType = models.CharField(max_length=100, choices=(('IT', 'IT'),('Non IT', 'Non IT')))
    companyActive = models.BooleanField(default=False)

    def __str__(self):
        return self.companyName


class Employee(models.Model):
    companyDetails = models.ForeignKey(Company, on_delete=models.CASCADE)
    employeeName = models.CharField(max_length=50)
    employeeEmail = models.EmailField()
    employeeAddress = models.CharField(max_length=200)
    employeeContact = models.IntegerField()
    employeeAbout = models.TextField()