from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='myapp/login.html', next_page='department_list'), name='login'),
    path('department-list/', views.department_list, name='department_list'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('department/new/', views.department_create, name='department_create'),
    path('department/<int:pk>/edit/', views.department_update, name='department_update'),
    path('department/<int:pk>/delete/', views.department_delete, name='department_delete'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
