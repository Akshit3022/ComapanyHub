from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

#     # companies/company_id/employees
#     @action(detail=True, methods=['GET'])
#     def employees(self, request, pk=None):
#         try:
#             company = Company.objects.get(pk=pk)
#             emps = Employee.objects.filter(companyDetails=company)
#             emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
#             return Response(emps_serializer.data)
#         except Exception as e:
#             print(e)
#             return Response({'message':'Company might not exists !!!'})


# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can create, update, delete

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]  # Any user can read
        return super().get_permissions()

    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(companyDetails=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not exists !!!'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAdminUser()]  # Only admin user can create
        elif self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]  # Any user can read
        return [permissions.IsAdminUser()]  # Only admin can update, delete