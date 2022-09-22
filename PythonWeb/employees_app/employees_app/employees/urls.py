from django.urls import path

from employees_app.employees.views import home, department, department_details, list_departments, show_departments, \
    redirect_to_first_department, redirect_to_department, show_not_found

urlpatterns = (
    path('redirect/', redirect_to_first_department, name='redirect'),
    path('info/', department, name='info'),
    path('details/<int:id>/', department_details, name='dep details'),
    path('list/', list_departments, name='dep list'),
    path('', show_departments, name='show dep'),
    path('redirect_dep/', redirect_to_department),
    path('not_found/', show_not_found, name='not found'),

)
