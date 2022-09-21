from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('This is home')

def department(request):
    return HttpResponse('This is department')

def department_details(request, id):
    return HttpResponse(f'This is department {id}')

def list_departments(request):
    return HttpResponse('This is department list')


