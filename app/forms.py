from django import forms
from .models import Company, Department

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['com_name']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'com_id']
        widgets = {
            'com_id': forms.Select()
        }
