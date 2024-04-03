from rest_framework import serializers
from api.models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = '__all__'

    def validate_companyName(self, value):

        instance = self.instance

        if instance and instance.companyName == value:
            return value
        
        allCompany = Company.objects.values_list('companyName', flat=True)  
        if value in allCompany:
            raise serializers.ValidationError("Company already exists") 
        return value

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_employeeEmail(self, value):
        employee = Employee.objects.values_list('employeeEmail', flat=True)
        if value in employee:
            raise serializers.ValidationError("Employee already exists")
        return value

    def validate_companyDetails(self, value):
        try:
            company = Company.objects.get(companyName=value)
            if not company.companyActive:
                raise serializers.ValidationError("Company is not active, you can not create employee for inactive company")
        except Company.DoesNotExist:
            raise serializers.ValidationError("Invalid company")
        return value
    
    def validate_employeeContact(self, value):
        newValue = str(value) 
        if len(newValue)!=10:
            raise serializers.ValidationError("Invalid Contact")
        