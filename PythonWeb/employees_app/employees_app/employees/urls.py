from django.urls import path

from employees_app.employees.views import home, department, department_details, list_departments

urlpatterns = (
    path('info/', department),
    path('details/<int:id>/', department_details),
    path('list/', list_departments),
)