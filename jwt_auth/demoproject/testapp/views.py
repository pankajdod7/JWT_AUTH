from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .authentication import CustomAuthentication



# Create your views here.

class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #authentication_classes = [JSONWebTokenAuthentication,]
    authentication_classes = [CustomAuthentication,]
    permission_classes = [IsAuthenticated,]
    

