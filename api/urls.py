from django.contrib import admin
from django.urls import path,include
from .views import CompanyViews
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'companies',CompanyViews)


urlpatterns = [
    path('', include(router.urls))
]
