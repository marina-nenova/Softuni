from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('This is home')

def department(request):
    return HttpResponse('This is department')
