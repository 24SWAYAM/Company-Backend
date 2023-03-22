from django.shortcuts import render
from api.models import Company
from rest_framework import viewsets
from api.serializer import CompanySerializer
# Create your views here.

class CompanyViews(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    