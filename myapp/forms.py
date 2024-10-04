from django import forms
from .models import Department, Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_id', 'salary']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'first_name', 'last_name', 'email', 'department']