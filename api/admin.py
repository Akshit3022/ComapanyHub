from django.contrib import admin
from api.models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'companyType')
admin.site.register(Company, CompanyAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeName', 'employeeEmail', 'employeeAddress', 'employeeContact', 'employeeAbout')
admin.site.register(Employee, EmployeeAdmin)

# Register your models here.
