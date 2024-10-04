from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Employee
from .forms import DepartmentForm, EmployeeForm
from django.contrib.auth.decorators import login_required
# For class-based views
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'myapp/department_list.html', {'departments': departments})


@login_required
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = department.employees.all()  # Using the related_name 'employees' to get related Employee objects
    return render(request, 'myapp/department_detail.html', {'department': department, 'employees': employees})


@login_required
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm()
    return render(request, 'myapp/department_form.html', {'form': form})


@login_required
def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save()
            return redirect('department_detail', pk=department.pk)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'myapp/department_form.html', {'form': form})

@login_required
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        department.delete()
        return redirect('department_list')
    return render(request, 'myapp/department_confirm_delete.html', {'department': department})

@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            # Assuming the Employee model has a foreign key to Department named 'department'
            department_pk = employee.department.pk
            return redirect('department_detail', pk=department_pk)
    else:
        form = EmployeeForm()
    return render(request, 'myapp/employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        department_pk = employee.department.pk  # Capture department pk before deletion
        employee.delete()
        return redirect('department_detail', pk=department_pk)
    return render(request, 'myapp/employee_confirm_delete.html', {'employee': employee})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to department_list upon successful login
                return redirect('department_list')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('logout')
