from django.contrib import admin
from api.models import Company, Employee

class Companyadmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    search_fields = ('name',)
class Employeeadmin(admin.ModelAdmin):
    list_display = ('name','email','company')
    list_filter = ('company',)

# Register your models here.
admin.site.register(Company, Companyadmin)
admin.site.register(Employee,Employeeadmin)
##admin - admin123