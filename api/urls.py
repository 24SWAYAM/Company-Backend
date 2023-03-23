from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViews, EmployeeViews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViews)
router.register(r'employees',EmployeeViews)
urlpatterns = [
    path('', include(router.urls))
]
