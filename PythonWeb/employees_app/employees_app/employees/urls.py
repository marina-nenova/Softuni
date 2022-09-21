from django.urls import path

from employees_app.employees.views import home, department

urlpatterns = (
    path('', home),
    path('department/', department)
)