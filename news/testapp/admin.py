from django.contrib import admin
from testapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename']
admin.site.register(Employee,EmployeeAdmin)