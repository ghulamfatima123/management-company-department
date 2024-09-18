from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Default route is the login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),  # Home page after login
    path('companies/', views.company_list, name='company_list'),
    path('departments/', views.department_list, name='department_list'),
    path('company/add/', views.company_form, name='company_add'),
    path('company/edit/<int:pk>/', views.company_form, name='company_edit'),
    path('company/delete/<int:pk>/', views.delete_company, name='company_delete'),
    path('department/add/', views.department_form, name='department_add'),
    path('department/edit/<int:pk>/', views.department_form, name='department_edit'),
    path('department/delete/<int:pk>/', views.delete_department, name='department_delete'),
]
