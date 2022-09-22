from django.urls import path

from employees_app.employees.views import home, department, department_details, list_departments, show_departments, \
    redirect_to_first_department

urlpatterns = (
    path('redirect/', redirect_to_first_department, name='redirect'),
    path('info/', department, name='info'),

    path('details/<int:id>/', department_details, name='dep details'),
    path('list/', list_departments, name='dep list'),
    path('', show_departments, name='show dep'),

)
