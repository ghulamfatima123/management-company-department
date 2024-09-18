from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Department
from .forms import CompanyForm, DepartmentForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def redirect_to_company_list(request):
    return redirect('company_list')
@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'app/company_list.html', {'companies': companies})
@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'app/department_list.html', {'departments': departments})

def company_form(request, pk=None):
    if pk:
        company = get_object_or_404(Company, pk=pk)
    else:
        company = None

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)

    return render(request, 'app/company_form.html', {'form': form})

def department_form(request, pk=None):
    if pk:
        department = get_object_or_404(Department, pk=pk)
    else:
        department = None

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'app/department_form.html', {'form': form})

def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return redirect('company_list')

def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('department_list')
